"""Build the run sheets.

Every night produces two files from the same data in sessions.py:

  plan/sessions/<theme>/<slug>.md   the page to read in the repository
  plan/sessions/<theme>/<slug>.pdf  one A4 page in two columns, to print

The PDF is rendered by headless Chrome. The HTML it renders from is written
next to the PDF, used, and deleted, so it never lands in the repository.

Run this from anywhere: python3 tools/build_sheets.py
"""

import html
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import layouts
from sessions import SESSIONS, THEMES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSION_DIR = os.path.join(ROOT, "plan", "sessions")
DIAGRAM_DIR = os.path.join(SESSION_DIR, "diagrams")
PHOTO_DIR = os.path.join(SESSION_DIR, "photos")

BROWSERS = ("google-chrome", "chromium", "chromium-browser", "google-chrome-stable")

CAPTIONS = {
    "lanes-15m": "Six lanes 15 metres long, with a cone at each end",
    "stop-line": "Six lanes with the stop line at 10 metres and 5 metres of run off",
    "hurdles": "A mini hurdle in the middle of each of the six lanes",
    "spots": "No lanes tonight, a disc for every boy and nothing to jump over",
    "loop-grid": "One loop about 70 metres round, everybody running the same way",
    "shuttle-grid": "Six lanes with turn cones at 5, 10 and 15 metres",
    "scatter-box": "An open box about 20 by 20 metres with a disc for every boy",
    "two-gates": "A start line and a gate at either side, 12 metres away",
    "move-pace": "Talking pace, and the question that checks it",
}

# What each photograph has to show. The photograph itself is optional.
PHOTO_CAPTIONS = {
    "move-first-step": "The first step goes forward, not up",
    "move-arms": "The hand goes from the pocket to the chin, on its own side of the body",
    "move-stop": "Two steps, knees bent, chest up, and held still",
    "move-landing": "Landing on the front of the feet, knees bent and knees apart",
}


def theme_of(session):
    return THEMES[session["theme"]]


def find_browser():
    for name in BROWSERS:
        path = shutil.which(name)
        if path:
            return path
    return None


def photos(session):
    """Return (good, bad) photo file names for this session, or (None, None).

    A photo is optional. Drop one into plan/sessions/photos and the next build
    puts it on every sheet that teaches that movement. See the README there.
    """
    key = session.get("photo")
    if not key:
        return None, None
    good = bad = None
    for ext in (".jpg", ".jpeg", ".png"):
        if good is None and os.path.exists(os.path.join(PHOTO_DIR, key + ext)):
            good = key + ext
        if bad is None and os.path.exists(os.path.join(PHOTO_DIR, key + "-bad" + ext)):
            bad = key + "-bad" + ext
    return good, bad


def neighbours(index):
    before = SESSIONS[index - 1] if index > 0 else None
    after = SESSIONS[index + 1] if index < len(SESSIONS) - 1 else None
    return before, after


def link_to(session, from_session):
    if theme_of(session)["key"] == theme_of(from_session)["key"]:
        return f'{session["slug"]}.md'
    return f'../{theme_of(session)["key"]}/{session["slug"]}.md'


# --------------------------------------------------------------------- markdown

def markdown(session, index):
    theme = theme_of(session)
    before, after = neighbours(index)
    good, bad = photos(session)
    out = [f'# Session {session["n"]}, {session["date"]}', ""]
    out.append(f'{session["code"]} · {session["kind"]} · Theme: {theme["name"]} · '
               f'Next match: {session["match"]}')
    out += ["", session["line"], ""]

    out += ["## On the ground", ""]
    out += [f"- {item}" for item in session["kit"]]
    out += ["", f'![{CAPTIONS[session["layout"]]}](../diagrams/{session["layout"]}.svg)', ""]
    if session.get("extra"):
        out += [f'![{CAPTIONS[session["extra"]]}](../diagrams/{session["extra"]}.svg)', ""]
    out += ["Set it up before the first group arrives and leave it for all three.", ""]

    out.append("## The seventeen minutes")
    for time, kind, name, lines in session["parts"]:
        out += ["", f"**{time}, {kind.lower()}: {name.lower()}.**", ""]
        out += [f"- {line}" for line in lines]
    out.append("")

    if good:
        out += ["## What it should look like", "",
                f'![{PHOTO_CAPTIONS[session["photo"]]}](../photos/{good})', ""]
        if bad:
            out += [f'![The same movement done badly](../photos/{bad})', ""]

    out += ["## Coach one thing", "", f'**{session["coach"]}**', ""]
    out += [f"- {item}" for item in session["watch"]]
    out += ["", f'**Lashing rain.** {session["wet"]}', "", "---", ""]
    tail = [f'[Print this sheet]({session["slug"]}.pdf)',
            "[How to run the station](../../session-guide.md)",
            "[All twenty nights](../../autumn-2026.md)"]
    if before:
        tail.append(f'[Back to session {before["n"]}]({link_to(before, session)})')
    if after:
        tail.append(f'[On to session {after["n"]}]({link_to(after, session)})')
    out.append(" · ".join(tail))
    return "\n".join(out) + "\n"


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
section.photo { border-left: 3px solid #2f7d4f; }
ul { margin: 0; padding-left: 1.1em; }
li { margin-bottom: 0.15em; }
.note { margin: 0.4em 0 0; font-size: 0.86em; color: #6a6f76; }
figure { margin: 0.45em 0 0; }
figure img { width: 100%; display: block; border-radius: 3px; }
.shots { display: flex; gap: 0.4em; }
.shots figure { flex: 1; margin: 0.45em 0 0; }
figcaption { font-size: 0.78em; color: #6a6f76; margin-top: 0.25em; }
.tag { font-weight: 700; font-size: 0.84em; }
.ok { color: #2f7d4f; } .no { color: #c0392b; }
.wet { font-size: 0.88em; color: #4a4f56; margin-top: 0.5em; padding-top: 0.35em;
       border-top: 1px dashed #e0b487; }
footer { border-top: 1px solid #d2d2ca; margin-top: 0.5em; padding-top: 0.35em; font-size: 0.78em;
         color: #6a6f76; display: flex; justify-content: space-between; gap: 1em; }
"""


# The sheet must be one A4 page. The build starts at the largest body size and
# steps down until the page fits, so a new photo or a longer part cannot spill
# onto a second page.
SIZES = (13.2, 12.8, 12.4, 12.0, 11.6, 11.2, 10.8, 10.4, 10.0, 9.6, 9.2, 8.8)


def sheet(session, base):
    theme = theme_of(session)
    e = html.escape
    good, bad = photos(session)

    facts = [("Code", session["code"]), ("Theme", theme["name"]),
             ("Next match", session["match"])]
    chips = f'<span class="fact night"><b>{e(session["kind"].split(".")[0])}</b></span>' + "".join(
        f'<span class="fact"><b>{e(k)}</b> {e(v)}</span>' for k, v in facts)

    blocks = [
        '<section class="setup"><h2>On the ground</h2><ul>'
        + "".join(f"<li>{e(item)}</li>" for item in session["kit"])
        + '</ul><p class="note">Set it up before the first group arrives and leave it for '
          'all three.</p>'
        + f'<figure><img src="../diagrams/{session["layout"]}.svg">'
          f'<figcaption>{e(CAPTIONS[session["layout"]])}</figcaption></figure>'
        + (f'<figure><img src="../diagrams/{session["extra"]}.svg">'
           f'<figcaption>{e(CAPTIONS[session["extra"]])}</figcaption></figure>'
           if session.get("extra") else "")
        + "</section>"
    ]

    for time, kind, name, lines in session["parts"]:
        blocks.append(
            f'<section class="part"><h2><span class="t">{e(time)}</span>'
            f'<span>{e(kind)}: {e(name.lower())}</span></h2><ul>'
            + "".join(f"<li>{e(line)}</li>" for line in lines) + "</ul></section>")

    if good:
        shots = f'<figure><img src="../photos/{good}">'
        if bad:
            shots = ('<div class="shots">'
                     f'<figure><img src="../photos/{good}">'
                     f'<figcaption class="tag ok">Like this</figcaption></figure>'
                     f'<figure><img src="../photos/{bad}">'
                     f'<figcaption class="tag no">Not this</figcaption></figure></div>')
        else:
            shots += f'<figcaption>{e(PHOTO_CAPTIONS[session["photo"]])}</figcaption></figure>'
        blocks.append(f'<section class="photo"><h2>What it should look like</h2>{shots}</section>')

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
<span>U11 athletic development &middot; 17 minutes</span></footer>
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


def build_pdf(browser, session, folder):
    html_path = os.path.join(folder, session["slug"] + ".html")
    pdf_path = os.path.join(folder, session["slug"] + ".pdf")
    try:
        for base in SIZES:
            with open(html_path, "w") as handle:
                handle.write(sheet(session, base))
            if render_pdf(browser, html_path, pdf_path) and page_count(pdf_path) == 1:
                settle_dates(pdf_path)
                return True
    finally:
        if os.path.exists(html_path):
            os.remove(html_path)
    return False


def main():
    layouts.build(DIAGRAM_DIR)
    browser = find_browser()
    if not browser:
        print("No Chrome or Chromium found, so the PDFs were not built.\n"
              "Install one of: " + ", ".join(BROWSERS), file=sys.stderr)

    for theme in THEMES:
        os.makedirs(os.path.join(SESSION_DIR, theme["key"]), exist_ok=True)

    failed = []
    for index, session in enumerate(SESSIONS):
        folder = os.path.join(SESSION_DIR, theme_of(session)["key"])
        with open(os.path.join(folder, session["slug"] + ".md"), "w") as handle:
            handle.write(markdown(session, index))
        if not browser:
            continue
        if not build_pdf(browser, session, folder):
            failed.append(session["slug"])

    print(f"built {len(SESSIONS)} markdown pages in {SESSION_DIR}")
    if browser:
        print(f"built {len(SESSIONS) - len(failed)} PDF sheets with {os.path.basename(browser)}")
    if failed:
        print("failed: " + ", ".join(failed), file=sys.stderr)


if __name__ == "__main__":
    main()
