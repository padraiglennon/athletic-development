"""Build the run sheets.

Every night produces two files from the same data in sessions.py:

  plan/sessions/<theme>/<slug>.md    the page to read in the repository
  plan/sessions/<theme>/<slug>.html  one A4 page in two columns, to print

Run this from the repository root: python3 tools/build_sheets.py
"""

import html
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import figures
import layouts
from sessions import SESSIONS, THEMES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSION_DIR = os.path.join(ROOT, "plan", "sessions")
DIAGRAM_DIR = os.path.join(SESSION_DIR, "diagrams")

CAPTIONS = {
    "lanes-15m": "Six lanes 15 metres long, a cone at each end, and a disc for every boy",
    "stop-line": "Six lanes with the stop line at 10 metres and 5 metres of run off",
    "hurdles": "A mini hurdle in the middle of each of the six lanes",
    "spots": "No lanes tonight, a disc for every boy and nothing to jump over",
    "loop-grid": "One loop about 70 metres round, everybody running the same way",
    "shuttle-grid": "Six lanes with turn cones at 5, 10 and 15 metres",
    "scatter-box": "An open box about 20 by 20 metres with a disc for every boy",
    "two-gates": "A start line and a gate at either side, 12 metres away",
    "move-pace": "Talking pace, and the question that checks it",
    "shape-sit": "The sit, done well and done badly",
    "shape-bow": "The bow, done well and done badly",
    "shape-plank": "The plank, done well and done badly",
    "shape-big-step": "The big step, done well and done badly",
    "shape-landing": "The landing, done well and done badly",
    "move-first-step": "The first step, done well and done badly",
    "move-stop": "Stopping on the line, done well and done badly",
    "move-arms": "Arms when running, done well and done badly",
}


def theme_of(session):
    return THEMES[session["theme"]]


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
    out = [f'# Session {session["n"]}, {session["date"]}', ""]
    out.append(f'{session["code"]} · {session["kind"]} · Theme: {theme["name"]} · '
               f'Body shape: {theme["shape"].lower()} · Next match: {session["match"]}')
    out += ["", session["line"], ""]

    out.append("## On the ground")
    out.append("")
    out += [f"- {item}" for item in session["kit"]]
    out.append("")
    out.append(f'![{CAPTIONS[session["layout"]]}](../diagrams/{session["layout"]}.svg)')
    out.append("")
    out.append("Set it up before the first group arrives and leave it for all three.")
    out.append("")

    out.append("## The seventeen minutes")
    for time, kind, name, lines in session["parts"]:
        out += ["", f"**{time}, {kind.lower()}: {name.lower()}.**", ""]
        out += [f"- {line}" for line in lines]
    out.append("")
    out.append(f'![{CAPTIONS[session["figure"]]}](../diagrams/{session["figure"]}.svg)')
    out.append("")

    out.append("## Coach one thing")
    out.append("")
    out.append(f'**{session["coach"]}**')
    out.append("")
    out += [f"- {item}" for item in session["watch"]]
    out.append("")
    out.append(f'**Lashing rain.** {session["wet"]}')
    out.append("")
    out.append("---")
    out.append("")
    tail = [f'[Print this sheet]({session["slug"]}.html)',
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
@page { size: A4 portrait; margin: 8mm 9mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: Helvetica, Arial, sans-serif; color: #22262b;
       font-size: 10.2pt; line-height: 1.38; background: #fff; }
header { display: flex; gap: 8px; align-items: stretch; border-bottom: 2px solid #22262b;
         padding-bottom: 4px; margin-bottom: 5px; }
.num { background: #22262b; color: #fff; font-size: 23pt; font-weight: 700; line-height: 1;
       padding: 6px 9px; border-radius: 4px; display: flex; align-items: center; }
.head h1 { font-size: 16pt; margin: 0 0 2px; letter-spacing: -0.2px; }
.facts { display: flex; flex-wrap: wrap; gap: 4px; }
.fact { font-size: 8.6pt; border: 1px solid #d2d2ca; border-radius: 3px; padding: 1px 5px;
        background: #fcfcf8; }
.fact b { font-weight: 700; }
.night { border-color: #a8560f; background: #fdf1e4; color: #7c3f0a; }
.line { font-size: 10.6pt; font-style: italic; color: #4a4f56; margin: 0 0 6px;
        border-left: 3px solid #e07a1f; padding-left: 7px; }
.cols { column-count: 2; column-gap: 6mm; column-fill: balance; }
.block { break-inside: avoid; margin-bottom: 6px; }
h2 { font-size: 10pt; text-transform: uppercase; letter-spacing: 0.7px; color: #6a6f76;
     margin: 0 0 3px; border-bottom: 1px solid #e2e2da; padding-bottom: 2px; }
.part h3 { font-size: 11pt; margin: 0 0 2px; }
.part h3 .t { display: inline-block; background: #eef2f7; color: #35506f; border-radius: 3px;
              padding: 0 4px; font-size: 8.8pt; margin-right: 4px; vertical-align: 1px; }
ul { margin: 0; padding-left: 12px; }
li { margin-bottom: 1.5px; }
figure { margin: 0 0 6px; break-inside: avoid; }
figure img { width: 100%; display: block; border: 1px solid #e2e2da; border-radius: 4px; }
figcaption { font-size: 8pt; color: #6a6f76; margin-top: 2px; }
.coach { background: #fdf1e4; border: 1px solid #e0b487; border-radius: 4px; padding: 5px 7px; }
.coach .one { font-weight: 700; font-size: 11.2pt; display: block; margin-bottom: 3px; }
.wet { font-size: 9pt; color: #4a4f56; margin-top: 4px; padding-top: 3px;
       border-top: 1px dashed #e0b487; }
footer { border-top: 1px solid #d2d2ca; margin-top: 5px; padding-top: 3px; font-size: 8pt;
         color: #6a6f76; display: flex; justify-content: space-between; }
"""


def block(inner, extra=""):
    return f'<div class="block{extra}">{inner}</div>'


def sheet(session, index):
    theme = theme_of(session)
    e = html.escape
    facts = [("Code", session["code"]), ("Theme", theme["name"]),
             ("Body shape", theme["shape"]), ("Next match", session["match"])]
    fact_html = "".join(
        f'<span class="fact"><b>{e(k)}</b> {e(v)}</span>' for k, v in facts)
    night = session["kind"].split(".")[0]
    fact_html = f'<span class="fact night"><b>{e(night)}</b></span>' + fact_html

    parts = []
    parts.append(block(
        '<h2>On the ground</h2><ul>'
        + "".join(f"<li>{e(item)}</li>" for item in session["kit"])
        + '</ul><p style="margin:3px 0 0;font-size:8.8pt;color:#6a6f76">'
          'Set it up before the first group arrives and leave it for all three.</p>'))
    parts.append(
        f'<figure><img src="../diagrams/{session["layout"]}.svg">'
        f'<figcaption>{e(CAPTIONS[session["layout"]])}</figcaption></figure>')

    for position, (time, kind, name, lines) in enumerate(session["parts"]):
        parts.append(block(
            f'<h3><span class="t">{e(time)}</span>{e(kind)}: {e(name.lower())}</h3>'
            + "<ul>" + "".join(f"<li>{e(line)}</li>" for line in lines) + "</ul>",
            " part"))
        if position == 2:
            parts.append(
                f'<figure><img src="../diagrams/{session["figure"]}.svg">'
                f'<figcaption>{e(CAPTIONS[session["figure"]])}</figcaption></figure>')

    parts.append(block(
        '<div class="coach"><span class="one">Coach one thing: '
        + e(session["coach"]) + "</span><ul>"
        + "".join(f"<li>{e(item)}</li>" for item in session["watch"])
        + f'</ul><div class="wet"><b>Lashing rain.</b> {e(session["wet"])}</div></div>'))

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<title>Session {session['n']}, {e(session['date'])}</title>
<style>{CSS}</style></head><body>
<header>
  <div class="num">{session['n']}</div>
  <div class="head">
    <h1>{e(session['date'])} &middot; {e(theme['name'])}</h1>
    <div class="facts">{fact_html}</div>
  </div>
</header>
<p class="line">{e(session['line'])}</p>
<div class="cols">
{chr(10).join(parts)}
</div>
<footer><span>{e(theme['aim'])}</span>
<span>U11 athletic development &middot; 17 minutes &middot; 25 boys &middot; run three times</span></footer>
</body></html>
"""


def main():
    figures.build(DIAGRAM_DIR)
    layouts.build(DIAGRAM_DIR)
    for theme in THEMES:
        os.makedirs(os.path.join(SESSION_DIR, theme["key"]), exist_ok=True)
    for index, session in enumerate(SESSIONS):
        folder = os.path.join(SESSION_DIR, theme_of(session)["key"])
        with open(os.path.join(folder, session["slug"] + ".md"), "w") as handle:
            handle.write(markdown(session, index))
        with open(os.path.join(folder, session["slug"] + ".html"), "w") as handle:
            handle.write(sheet(session, index))
    print(f"built {len(SESSIONS)} run sheets in {SESSION_DIR}")


if __name__ == "__main__":
    main()
