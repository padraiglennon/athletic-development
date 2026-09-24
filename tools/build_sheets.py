"""Build the run sheets.

Every night is a hand-edited markdown file:

  plan/sessions/<theme>/<slug>.md   the source a coach edits
  plan/sessions/<theme>/<slug>.pdf  one A4 page in two columns, to print

The build owns two marked regions of each source file, the header at the top
and the link row at the bottom, and rewrites both. It never touches the text
between the markers. See design/ADR-001-markdown-session-sources.md.

The PDF is rendered by headless Chrome. The HTML it renders from is written
next to the PDF, used, and deleted, so it never lands in the repository.

Run this from anywhere: python3 tools/build_sheets.py
Build one session only: python3 tools/build_sheets.py 06-thu-10-sep
(also accepts a session number, e.g. python3 tools/build_sheets.py 6)
"""

import glob
import html
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import layouts
import sessionfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSION_DIR = os.path.join(ROOT, "plan", "sessions")
DIAGRAM_DIR = os.path.join(SESSION_DIR, "diagrams")
THEMES_PATH = os.path.join(SESSION_DIR, "themes.md")
CALENDAR_PATH = os.path.join(ROOT, "plan", "autumn-2026.md")

BROWSERS = ("google-chrome", "chromium", "chromium-browser", "google-chrome-stable")

PUSH_NIGHT = "Push night. Teach it slowly, then put the pace up"
EASE_NIGHT = "Ease off night. Match pace, then send them home fresher"

SETUP_NOTE = "1 minute setup. Set it up before the first group arrives and leave it for all three."


def find_browser():
    for name in BROWSERS:
        path = shutil.which(name)
        if path:
            return path
    return None


# ---------------------------------------------------------------------- themes

THEME_HEADING_RE = re.compile(r'^##\s+(?P<key>\S+)\s*·\s*(?P<name>.+)$')


def load_themes(path):
    """Read plan/sessions/themes.md into an ordered {key: {key, name, aim}} dict."""
    with open(path) as handle:
        lines = handle.read().split("\n")
    themes = {}
    key = name = None
    aim_lines = []

    def close():
        if key is not None:
            themes[key] = {"key": key, "name": name, "aim": " ".join(aim_lines).strip()}

    for line in lines:
        match = THEME_HEADING_RE.match(line.strip())
        if match:
            close()
            key, name = match.group("key"), match.group("name").strip()
            aim_lines = []
        elif key is not None and line.strip() and not line.strip().startswith("#"):
            aim_lines.append(line.strip())
    close()
    return themes


# -------------------------------------------------------------------- sessions

def discover_session_files(themes):
    paths = []
    for theme in themes.values():
        paths += sorted(glob.glob(os.path.join(SESSION_DIR, theme["key"], "*.md")))
    return paths


def load_sessions(themes):
    """Parse every session file. Returns (sessions_by_slug, errors).

    All 20 files are read and validated before anything is written, so one
    broken file is reported alongside every other fault in a single run.
    """
    errors = []
    sessions = {}
    seen_n = {}

    for path in discover_session_files(themes):
        rel = os.path.relpath(path, ROOT)
        with open(path) as handle:
            text = handle.read()
        session, file_errors, images = sessionfile.parse_session_file(text, rel)

        for alt, src in images:
            image_path = os.path.normpath(os.path.join(os.path.dirname(path), src))
            if not os.path.exists(image_path):
                errors.append(f"{rel}: image not found: {src}")

        if file_errors:
            errors += file_errors
            continue

        slug = os.path.splitext(os.path.basename(path))[0]
        folder_key = os.path.basename(os.path.dirname(path))
        if session["theme"] != folder_key:
            errors.append(f"{rel}: frontmatter theme '{session['theme']}' does not match "
                           f"the folder it is in, '{folder_key}'")
            continue
        if session["theme"] not in themes:
            errors.append(f"{rel}: theme '{session['theme']}' is not in {THEMES_PATH}")
            continue
        if session["n"] in seen_n:
            errors.append(f"{rel}: session number {session['n']} is also used by "
                           f"{seen_n[session['n']]}")
        else:
            seen_n[session["n"]] = rel

        session["slug"] = slug
        session["path"] = path
        sessions[slug] = session

    return sessions, errors


def kind_text(session):
    if session["kind"]:
        return session["kind"]
    return PUSH_NIGHT if session["night"] == "push" else EASE_NIGHT


def ordered_slugs(sessions):
    return [slug for slug, _ in sorted(sessions.items(), key=lambda kv: kv[1]["n"])]


def neighbours(order, slug):
    index = order.index(slug)
    before = order[index - 1] if index > 0 else None
    after = order[index + 1] if index < len(order) - 1 else None
    return before, after


def link_to(session, target_slug, sessions):
    target = sessions[target_slug]
    if session["theme"] == target["theme"]:
        return f"{target_slug}.md"
    return f"../{target['theme']}/{target_slug}.md"


# ------------------------------------------------------------------ marked regions

def build_header(session, theme):
    return (f'# Session {session["n"]}, {session["date"]}\n\n'
            f'{session["code"]} · {kind_text(session)} · Theme: {theme["name"]} · '
            f'Next match: {session["match"]}')


def build_links(session, order, sessions):
    before, after = neighbours(order, session["slug"])
    tail = [f'[Print this sheet]({session["slug"]}.pdf)',
            "[How to run the station](../../session-guide.md)",
            "[All twenty nights](../../autumn-2026.md)"]
    if before:
        tail.append(f'[Back to session {sessions[before]["n"]}]'
                     f'({link_to(session, before, sessions)})')
    if after:
        tail.append(f'[On to session {sessions[after]["n"]}]'
                     f'({link_to(session, after, sessions)})')
    return " · ".join(tail)


def rewrite_source(session, theme, order, sessions):
    with open(session["path"]) as handle:
        text = handle.read()
    middle, errors = sessionfile.split_marked_regions(text, session["path"])
    if errors:
        return errors

    new_text = (
        f"{sessionfile.HEADER_OPEN}\n{build_header(session, theme)}\n"
        f"{sessionfile.HEADER_CLOSE}\n\n"
        f"{middle}\n\n"
        f"{sessionfile.LINKS_OPEN}\n{build_links(session, order, sessions)}\n"
        f"{sessionfile.LINKS_CLOSE}\n"
    )
    if new_text != text:
        with open(session["path"], "w") as handle:
            handle.write(new_text)
    return []


# ------------------------------------------------------------------------- html

CSS = """
@page { size: A4 portrait; margin: 9mm 10mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: Helvetica, Arial, sans-serif; color: #22262b;
       font-size: BASE; line-height: 1.36; background: #fff;
       min-height: 100vh; display: flex; flex-direction: column; }

header { display: flex; gap: 0.9em; align-items: stretch; margin-bottom: 0.6em; }
.num { background: #22262b; color: #fff; font-size: 2.35em; font-weight: 700; line-height: 1;
       padding: 0.3em 0.45em; border-radius: 5px; display: flex; align-items: center; }
.head { flex: 1; }
.head h1 { font-size: 1.57em; margin: 0 0 0.18em; letter-spacing: -0.2px; }
.facts { display: flex; flex-wrap: wrap; gap: 0.4em; }
.fact { font-size: 0.84em; border: 1px solid #d2d2ca; border-radius: 3px; padding: 0.1em 0.55em;
        background: #fcfcf8; }
.fact b { font-weight: 700; }
.night { border-color: #a8560f; background: #fdf1e4; color: #7c3f0a; }
.line { font-size: 1.04em; font-style: italic; color: #4a4f56; margin: 0 0 0.7em;
        border-left: 3px solid #e07a1f; padding-left: 0.7em; }

.cols { column-count: 2; column-gap: 6mm; flex: 1; }

/* Every section is its own card, so a coach can find one part at a glance. */
section { break-inside: avoid; border: 1px solid #dcdcd4; border-radius: 5px;
          padding: 0.55em 0.7em 0.65em; margin-bottom: 0.55em; background: #fff; }
section > h2 { font-size: 0.86em; text-transform: uppercase; letter-spacing: 0.8px;
               color: #6a6f76; margin: 0 0 0.4em; }
section.part { border-left: 3px solid #4b7fc4; }
section.part h2 { display: flex; gap: 0.5em; align-items: baseline; text-transform: none;
                  letter-spacing: 0; font-size: 1.08em; color: #22262b; font-weight: 700;
                  margin-bottom: 0.3em; }
section.part h2 .t { background: #eef2f7; color: #35506f; border-radius: 3px;
                     padding: 0 0.4em; font-size: 0.8em; font-weight: 700; white-space: nowrap; }
section.setup { border-left: 3px solid #e07a1f; }
section.coach { border-left: 3px solid #a8560f; background: #fdf1e4; border-color: #e0b487; }
section.coach .one { font-weight: 700; font-size: 1.1em; display: block; margin-bottom: 0.35em; }
ul { margin: 0; padding-left: 1.1em; }
li { margin-bottom: 0.15em; }
.note { margin: 0.4em 0 0; font-size: 0.86em; color: #6a6f76; }
figure { margin: 0.45em 0 0; }
figure img { width: 100%; display: block; border-radius: 3px; }
figcaption { font-size: 0.78em; color: #6a6f76; margin-top: 0.25em; }
.wet { font-size: 0.88em; color: #4a4f56; margin-top: 0.5em; padding-top: 0.35em;
       border-top: 1px dashed #e0b487; }
footer { border-top: 1px solid #d2d2ca; margin-top: 0.5em; padding-top: 0.35em; font-size: 0.78em;
         color: #6a6f76; display: flex; justify-content: space-between; gap: 1em; }
"""


# The sheet must be one A4 page. The build starts at the largest body size and
# steps down until the page fits, so a longer part cannot spill onto a second page.
SIZES = (13.2, 12.8, 12.4, 12.0, 11.6, 11.2, 10.8, 10.4, 10.0, 9.6, 9.2, 8.8)


def sheet(session, theme, base):
    e = html.escape

    facts = [("Code", session["code"]), ("Theme", theme["name"]),
             ("Next match", session["match"])]
    chips = (f'<span class="fact night"><b>{e(kind_text(session).split(".")[0])}</b></span>'
             + "".join(f'<span class="fact"><b>{e(k)}</b> {e(v)}</span>' for k, v in facts))

    figures = "".join(
        f'<figure><img src="{e(src)}"><figcaption>{e(alt)}</figcaption></figure>'
        for alt, src in session["images"])

    blocks = [
        '<section class="setup"><h2>On the ground</h2><ul>'
        + "".join(f"<li>{e(item)}</li>" for item in session["kit"])
        + f'</ul><p class="note">{e(SETUP_NOTE)}</p>'
        + figures
        + "</section>"
    ]

    for time, kind, name, lines in session["parts"]:
        blocks.append(
            f'<section class="part"><h2><span class="t">{e(time)}</span>'
            f'<span>{e(kind)}: {e(name.lower())}</span></h2><ul>'
            + "".join(f"<li>{e(line)}</li>" for line in lines) + "</ul></section>")

    blocks.append(
        '<section class="coach"><span class="one">Coach one thing: '
        + e(session["coach"]) + "</span><ul>"
        + "".join(f"<li>{e(item)}</li>" for item in session["watch"])
        + f'</ul><div class="wet"><b>Lashing rain.</b> {e(session["wet"])}</div></section>')

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Session {session['n']}, {e(session['date'])}</title>
<style>{CSS.replace("BASE", f"{base}pt")}</style></head><body>
<header>
  <div class="num">{session['n']}</div>
  <div class="head">
    <h1>{e(session['date'])} &middot; {e(theme['name'])}</h1>
    <div class="facts">{chips}</div>
  </div>
</header>
<p class="line">{e(session['line'])}</p>
<div class="cols">
{chr(10).join(blocks)}
</div>
<footer><span>{e(theme['aim'])}</span>
<span>U11 athletic development &middot; 11 minutes</span></footer>
</body></html>
"""


def render_pdf(browser, html_path, pdf_path):
    subprocess.run(
        [browser, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", "file://" + html_path],
        capture_output=True, check=False)
    return os.path.exists(pdf_path)


# Chrome stamps the build time into every PDF. The stamp is replaced with a
# fixed date of the same length, so a rebuild that changes nothing produces the
# same bytes and git stays quiet.
FIXED_DATE = b"D:20260101000000+00'00'"


def settle_dates(pdf_path):
    with open(pdf_path, "rb") as handle:
        data = handle.read()
    fixed = re.sub(rb"D:\d{14}\+00'00'", FIXED_DATE, data)
    if fixed != data:
        with open(pdf_path, "wb") as handle:
            handle.write(fixed)


def page_count(pdf_path):
    """Read the page count out of the raw PDF, so no PDF library is needed."""
    with open(pdf_path, "rb") as handle:
        found = re.findall(rb"/Count\s+(\d+)", handle.read())
    return int(found[0]) if found else 0


def build_pdf(browser, session, theme, folder):
    """Render the PDF into a temp file first, so a session that never fits
    one page leaves the PDF already on disk untouched."""
    html_path = os.path.join(folder, session["slug"] + ".html")
    tmp_path = os.path.join(folder, session["slug"] + ".tmp.pdf")
    pdf_path = os.path.join(folder, session["slug"] + ".pdf")
    try:
        for base in SIZES:
            with open(html_path, "w") as handle:
                handle.write(sheet(session, theme, base))
            if render_pdf(browser, html_path, tmp_path) and page_count(tmp_path) == 1:
                settle_dates(tmp_path)
                os.replace(tmp_path, pdf_path)
                return True
    finally:
        if os.path.exists(html_path):
            os.remove(html_path)
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
    return False


# --------------------------------------------------------------------- calendar

CALENDAR_ROW_RE = re.compile(
    r'^\|\s*(?P<n>\d+)\s*\|\s*\[(?P<short_date>[^\]]+)\]\((?P<link>[^)]+)\)\s*\|'
    r'\s*(?P<code>[^|]+?)\s*\|\s*(?P<saturday>[^|]+?)\s*\|\s*(?P<theme>[^|]+?)\s*\|\s*$')

MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")


def short_date(full_date):
    """'Tuesday 25 August' -> 'Tue 25 Aug', with no datetime year guessing needed."""
    weekday, day, month = full_date.split(" ", 2)
    return f"{weekday[:3]} {int(day):d} {month[:3]}"


def short_match(match):
    """'Football, Saturday 29 August' -> 'Football, 29 Aug'."""
    code, _, rest = match.partition(", ")
    _, day, month = rest.split(" ", 2)
    return f"{code}, {int(day):d} {month[:3]}"


def check_calendar_drift(sessions):
    if not os.path.exists(CALENDAR_PATH):
        return
    with open(CALENDAR_PATH) as handle:
        lines = handle.read().split("\n")

    warnings = []
    for line in lines:
        match = CALENDAR_ROW_RE.match(line)
        if not match:
            continue
        slug = os.path.splitext(os.path.basename(match.group("link")))[0]
        session = sessions.get(slug)
        if session is None:
            warnings.append(f"plan/autumn-2026.md: row for session {match.group('n')} "
                             f"links to {slug}, which has no session file")
            continue

        rel = os.path.relpath(session["path"], ROOT)
        expected = {
            "n": str(session["n"]),
            "short_date": short_date(session["date"]),
            "code": session["code"],
            "saturday": short_match(session["match"]),
            "theme": sessions[slug]["theme_name"],
        }
        for field, value in expected.items():
            if match.group(field) != value:
                warnings.append(f"plan/autumn-2026.md: session {session['n']} row has "
                                 f"{field}={match.group(field)!r}, but {rel} has {value!r}")

    for warning in warnings:
        print("warning: " + warning, file=sys.stderr)


# ------------------------------------------------------------------------- main

def select_sessions(sessions, order, wanted):
    """Match each argument against a session slug or number. All sessions if none given."""
    if not wanted:
        return list(order)
    chosen = []
    unmatched = list(wanted)
    for slug in order:
        for arg in wanted:
            if arg == slug or arg == str(sessions[slug]["n"]):
                chosen.append(slug)
                if arg in unmatched:
                    unmatched.remove(arg)
                break
    if unmatched:
        sys.exit("no session matches: " + ", ".join(unmatched))
    return chosen


def main():
    layouts.build(DIAGRAM_DIR)

    themes = load_themes(THEMES_PATH)
    sessions, errors = load_sessions(themes)
    if errors:
        print(f"{len(errors)} fault(s) found, nothing was built:", file=sys.stderr)
        for error in sorted(errors):
            print("  " + error, file=sys.stderr)
        sys.exit(1)

    for session in sessions.values():
        session["theme_name"] = themes[session["theme"]]["name"]

    order = ordered_slugs(sessions)
    check_calendar_drift(sessions)

    wanted = select_sessions(sessions, order, sys.argv[1:])
    browser = find_browser()
    if not browser:
        print("No Chrome or Chromium found, so the PDFs were not built.\n"
              "Install one of: " + ", ".join(BROWSERS), file=sys.stderr)

    failed = []
    for slug in wanted:
        session = sessions[slug]
        theme = themes[session["theme"]]
        folder = os.path.dirname(session["path"])
        rewrite_errors = rewrite_source(session, theme, order, sessions)
        if rewrite_errors:
            for error in rewrite_errors:
                print("error: " + error, file=sys.stderr)
            failed.append(slug)
            continue
        if not browser:
            continue
        if not build_pdf(browser, session, theme, folder):
            failed.append(slug)

    print(f"built {len(wanted)} session(s) in {SESSION_DIR}")
    if browser:
        print(f"built {len(wanted) - len(failed)} PDF sheet(s) with {os.path.basename(browser)}")
    if failed:
        print("failed: " + ", ".join(failed), file=sys.stderr)


if __name__ == "__main__":
    main()
