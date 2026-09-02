# U11 athletic development

Plans for the athletic development part of U11 training, for a squad of 75 to 80 hurling and football boys. Built on the GAA's athletic development action statement, published in 2024.

## What the week looks like

Training is at 5.30 on Tuesday and Thursday. There is a match every Saturday, hurling one week and football the next.

| | Tuesday | Thursday | Saturday |
| --- | --- | --- | --- |
| Code | The one that played last Saturday | The one playing this Saturday | |
| Format | Normal rotations | Match format, same as Saturday | Match, hurling and football on alternate weeks |
| Our job | Teach the movement slowly, then push it | Use it at match pace, then ease off | |

Both nights run the same shape:

| | |
| --- | --- |
| 5 to 8 minutes | Warm-up, all 80 boys together |
| 17 to 18 minutes | Rotation 1 |
| 17 to 18 minutes | Rotation 2 |
| 17 to 18 minutes | Rotation 3 |

Three groups, sorted by ability, rotating between athletic development, skills, and a match. So the athletic development station is about 25 boys at a time, seventeen minutes, run three times a night, twice a week.

## Read these

1. [plan/session-guide.md](plan/session-guide.md) is how to run the seventeen minutes with 25 boys, and how Tuesday differs from Thursday. Read this one first, and read it again before your first night.
2. [plan/activities.md](plan/activities.md) is the bank of themes, one every four sessions, each filling the seventeen minutes.
3. [plan/year-plan.md](plan/year-plan.md) is what order the themes go in and why.
4. [plan/autumn-2026.md](plan/autumn-2026.md) is the calendar from 25 August to Halloween, and it links to every night.
5. [plan/sessions/](plan/sessions/) is one sheet per night, in a folder per theme. Print the `.pdf` file: it is a single A4 page in two columns, with a card for each part of the seventeen minutes and a picture of the layout. This is the page to bring to the pitch.
6. [plan/equipment.md](plan/equipment.md) is what to buy with the 100 euro.
7. [knowledge/action-statement-notes.md](knowledge/action-statement-notes.md) is the GAA document explained in ordinary words, for when someone asks why we do it this way.

## The short version

The match rotation makes them fit. The skills rotation teaches them hurling and football. Our seventeen minutes teach them to start, stop, sprint and land without hurting themselves, and to hold seven body shapes.

A theme is four sessions: two Tuesdays and two Thursdays. The autumn runs starting, endurance, sprints, stopping, jumping, and finishes on the Thursday before Halloween.

Tuesday teaches it slowly and is the night to push. Thursday uses it at speed, with a hurl or a ball in hand, and eases off, because there is a match two days later every week.

Nothing heavier than their own body. Slower and correct beats faster and messy. Nobody gets tested, measured or ranked.

## Building the run sheets

The twenty run sheets are generated, not written by hand. The content of every night is in [tools/sessions.py](tools/sessions.py) and the layout diagrams are drawn by [tools/layouts.py](tools/layouts.py).

```
python3 tools/build_sheets.py
```

That writes the `.md` page and the A4 `.pdf` sheet for all twenty nights, and redraws every diagram. It needs Python 3 and Google Chrome, which prints the PDF. Editing a `.md` or a `.pdf` by hand does not last, because the next build writes over it.

To put a photograph on a sheet, read [plan/sessions/photos/README.md](plan/sessions/photos/README.md).

## Assumptions

Everything in this plan rests on these. If one of them is wrong, the parts that depend on it are wrong with it.

- Two sessions a week, Tuesday and Thursday at 5.30, all year apart from December.
- A match every Saturday, alternating hurling and football.
- One or two coaches at the athletic development station.
- The club already owns a pitch, balls and hurls. The 100 euro is for extras only.
- Groups are sorted by ability and stay roughly the same week to week.
- The season runs all year, January to January. There is no off season to hide a hard block in.
