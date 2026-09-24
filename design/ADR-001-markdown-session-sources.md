# ADR-001: Generate the run sheets from markdown source files

**Status:** Draft
**Date:** 2026-09-10
**Author:** Padraig Lennon
**Tracking issue:** #1

## Context

The 20 autumn run sheets are generated, not written by hand. `tools/sessions.py` holds every night as a Python dict in a 40 KB file. `tools/build_sheets.py` reads that data and writes 2 files for each night: a markdown page to read in the repository, and an A4 PDF to print. `tools/layouts.py` draws the SVG pitch diagrams.

This locks the words behind code. A coach who wants to cut one bullet from one night must open a Python file, find the right dict, and keep the quotes and the commas right. The content of a night and the code that lays out the page sit in the same file.

A second gap follows from the same cause. The club wants photographs on the sheets, to show a coach what a good first step or a good landing looks like. A photograph is a file, and there is no way to point at a file from a Python dict without more Python. An earlier version of `build_sheets.py` solved this with a `photo` key and a `PHOTO_CAPTIONS` table that named 4 fixed body shape photographs. The uncommitted working tree removes that code, because the body shapes came out of the autumn. The lesson from it is that a fixed table of file names is too rigid: it allows a photograph only where the table already expects one.

This work sits on top of an uncommitted working tree. That tree removes the photo code, adds the `chase-ring` and `shuttle-weave` diagrams to `layouts.py`, and rewrites session 6. This ADR assumes that work lands first or lands with it.

The build must stay easy to run. `README.md` promises Python 3 and Google Chrome, and nothing else. `build_sheets.py` already replaces the Chrome build time stamp in each PDF with a fixed date, so a rebuild that changes nothing produces the same bytes and git stays quiet. That property makes a faithful migration provable.

## Decision

Each night becomes one hand-edited markdown file at `plan/sessions/<theme>/<slug>.md`, at the same path the build writes today. The build reads that file and writes the A4 PDF beside it. `tools/sessions.py` is deleted.

The markdown holds the content of a night. It holds no page layout. The cards, the 2 columns, the colours and the font sizes stay in `build_sheets.py`.

### The source file

A `---` fenced block at the top carries the facts a coach does not write as prose. A reader of about 25 lines parses `key: value` lines and simple lists. The build gains no dependency.

```markdown
---
n: 1
date: Tuesday 25 August
theme: 1-starting
code: Hurling
night: push
match: Football, Saturday 29 August
kit:
  - 12 cones, six lanes, 15 metres
  - Hurls down for now
coach: The first step goes forward, not up.
wet: Everything here works in the wet. Keep them off the ground.
---

The first night at the station. Half the job tonight is teaching them where to stand.

![Six lanes 15 metres long, with a cone at each end](../diagrams/lanes-15m.svg)

## The station

### 1 to 6 · Movement · Two starts

- Six lanes, four boys to a lane, one wave goes on every whistle.

### 6 to 11 · Challenge game · Standing race

- Pairs, one pair to a lane, standing start.

## Coach one thing

- Boys who bounce upright before they run. They have wasted a step.
- Heels lifting as he sets his feet. Move his feet a bit wider.
```

The body has 3 parts.

1. Everything before the first `##` is the setup. The first paragraph is the sentence of context that opens the sheet. Any image there prints in the "On the ground" card, under the kit list from frontmatter.
2. `## The station` holds one `###` heading for each exercise. The heading carries 3 facts separated by a middle dot: the minutes, the kind of part, and the name. The bullets under it are what the coach says and does.
3. `## Coach one thing` holds the faults to watch. The one thing itself comes from the `coach` key, and the rain note comes from the `wet` key.

`night` takes the value `push` or `ease`. The build holds the 2 sentences those words stand for, so each sentence exists in one place. A night that fits neither, such as session 6 breaking its usual place in the theme for a full speed night, sets `kind` instead, a one-line sentence of its own that the build prints as it is. A file must set exactly one of `night` or `kind`. `theme` names the folder, so the build can check the file sits in the right one. `slug` and `short` are gone: the filename is the slug, and no code reads `short`.

`plan/sessions/themes.md` takes the 5 theme keys, names and aims. The aim prints in the PDF footer.

### Pictures

Every picture is a normal markdown image in the body. A PNG photograph and a generated SVG diagram use the same syntax. The alt text becomes the caption on the sheet.

PNG files live in `plan/sessions/photos/`. The build does not open or resize them. `build_sheets.py` writes the HTML it prints from into the same folder as the PDF, so a relative path in the markdown resolves for Chrome without change.

This deletes the `layout` and `extra` keys and the `CAPTIONS` table in `build_sheets.py`. `layouts.py` and `svgkit.py` keep drawing the SVG files into `plan/sessions/diagrams/` and do not change.

### What the build writes

The build writes the `.pdf` for each night, and it writes 2 marked regions inside each source file. A header block at the top carries the title and the facts line. A link row at the bottom carries the print link, the guide link, and the links to the night before and the night after. The build replaces the text between each pair of markers and never touches anything else in the file.

```markdown
<!-- built: header -->
# Session 1, Tuesday 25 August

Hurling · Push night · Theme: Starting · Next match: Football, Saturday 29 August
<!-- /built -->
```

### What the build checks

The build reads all 20 files before it writes anything. It collects every fault it finds and prints each one with the file name: an absent frontmatter key, an unknown key, an image file that is not on disk, a heading it does not recognise, an exercise heading with the wrong number of parts, a `theme` value that does not match the folder. If there is 1 fault or more, the build stops and writes no file.

It compares the table of 20 nights in `plan/autumn-2026.md` against the frontmatter and prints a warning naming any row that disagrees. That table stays hand-written, and a warning does not stop the build.

`build_sheets.py` steps the body size down from 13.2pt to 8.8pt until the sheet fits 1 A4 page. When a night does not fit at 8.8pt the build now fails, names the session, and leaves the old PDF alone. The 1 page promise holds and the coach cuts a bullet.

## Requirements

### Functional

- A frontmatter reader parses a `---` fenced block of `key: value` lines and simple `- item` lists into a dict. It uses the standard library only.
- A session reader parses one markdown file into the same shape `build_sheets.py` renders today, and reports faults instead of raising.
- `build_sheets.py` reads the 20 files, validates them all, then writes the PDFs and the marked regions.
- `plan/sessions/themes.md` supplies the theme key, name and aim.
- Markdown images in the body render as picture cards with the alt text as the caption, for `.png` and `.svg` alike.
- A one-off script converts the 20 nights from `tools/sessions.py` to markdown. The script and `tools/sessions.py` are both deleted in the same commit.
- `README.md` gains the shape of a source file and the rule that the build owns the marked regions. It no longer names `tools/sessions.py`.
- `plan/sessions/photos/` gains a short README that says where photographs go and that a parent must give written permission before anyone photographs a boy.

### Non-functional

- The build keeps its 2 requirements: Python 3 and Google Chrome. No pip install.
- A rebuild that changes no source file produces the same PDF bytes, so git stays quiet.
- No telemetry. This is a script a coach runs on a laptop.
- The photographs are of children. They stay in this repository and go nowhere else.

## Acceptance Criteria

### User-visible AC

- [ ] The one-off script converts the 20 nights, and the PDFs rebuilt from the markdown match a baseline byte for byte. The baseline is a full build from `tools/sessions.py` at the tip of the work in progress, taken before any file is deleted. The PDFs on disk are not the baseline, because the working tree has changed `layouts.py` and `sessions.py` and only session 6 was rebuilt after it.
- [ ] A coach changes 1 bullet in a markdown file, runs `python3 tools/build_sheets.py`, and the new PDF shows the change.
- [ ] A coach saves a PNG in `plan/sessions/photos/`, adds 1 image line to a session file, and the picture prints on that sheet with the alt text as its caption.
- [ ] A file with an absent frontmatter key and an image path that is not on disk reports both faults in a single run, and the build writes no file.
- [ ] A session with too much content to fit 1 A4 page at 8.8pt fails by name, and the PDF already on disk is unchanged.
- [ ] A row of the table in `plan/autumn-2026.md` that disagrees with the frontmatter produces a warning that names the row, and the build still writes the PDFs.
- [ ] The build rewrites the header and the link row in a source file and leaves every other line of that file unchanged.
- [ ] `tools/sessions.py` no longer exists, and `python3 tools/build_sheets.py` builds 20 PDFs.

### Review checklist

- [ ] Thorough code security review of the new code
- [ ] Relevant documentation updated
- [ ] Anti-hallucination review against actual code state

## Alternatives Considered

**Keep the source in Python and add a photo key.** This is the smallest change and it solves the photographs. It does not solve the real problem, because a coach still edits Python to change a word.

**Put the hand-edited files in a new folder and keep generating the reader page.** The build would write both the reader `.md` and the `.pdf`, exactly as it does today, with no risk that a build and an edit fight each other. Rejected because it puts 2 markdown files on disk for every night, and a coach who opens the wrong one loses the edit.

**YAML frontmatter parsed by PyYAML.** Familiar to anyone who has used a static site generator, and a full parser. Rejected because it breaks the promise in `README.md` that the build needs Python 3 and Chrome only.

**TOML frontmatter parsed by the standard library `tomllib`.** A real parser with no new dependency, and Python 3.12 is on the machine. Rejected because GitHub prints a `+++` block as text at the top of the page, while it hides a `---` block. The page a coach reads on GitHub would open with 10 lines of configuration.

**Fixed `##` headings for every card, with the kit list and the coach note in the body.** Rejected in favour of frontmatter for the short fields, because a 1 line field reads better as a key than as a section with 1 bullet in it.

**Keep `tools/sessions.py` as a fallback for nights with no markdown file.** Rejected because it leaves 2 sources of truth and the migration never finishes.

**Resize large photographs during the build with Pillow.** A phone photograph can make a large PDF. Rejected for now because it adds a dependency to solve a problem nobody has yet.

## Consequences

A coach can change any night with a text editor. The words and the page layout are now in separate files.

The build writes into a file a person edits. This is the main risk this decision accepts. The markers bound the damage, and a bad rewrite is visible in `git diff` before anyone commits it, but the risk is real and the earlier design avoided it.

`build_sheets.py` grows a reader and a validator, so it does more than it did. The `markdown` function that wrote the reader page shrinks to the 2 marked regions.

The dates, codes and fixtures now live in 2 places: the frontmatter of 20 files, and the hand-written table in `plan/autumn-2026.md`. The build warns about drift instead of preventing it. If the warning proves easy to ignore, the next step is to generate that table between markers, the same way the header and the link row work.

Photographs of children enter the repository. The repository is public on GitHub. `plan/sessions/photos/README.md` must state the permission rule plainly, and nobody should add a photograph of a boy before a parent gives written permission.

Writing a night by hand is now possible, and it is also now the only way. There is no template, so the first new season after the autumn starts from a copy of an old file.
