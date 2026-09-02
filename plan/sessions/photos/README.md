# Photos for the run sheets

Drop a photo in here and the next build puts it on the matching run sheet, under
the heading "What it should look like". No photo means the sheet is built without
one, which is what happens today.

## The file names the build looks for

| File | What to photograph | Sheets that use it |
| --- | --- | --- |
| `shape-sit.jpg` | The sit, held at the bottom | 1, 2, 3, 4 |
| `shape-plank.jpg` | The plank, from the side | 6, 7 |
| `shape-big-step.jpg` | The big step, from the front | 10, 12 |
| `shape-bow.jpg` | The bow, from the side | 14, 16 |
| `shape-landing.jpg` | A landing, held still | 17, 18, 19, 20 |
| `move-first-step.jpg` | The first step out of a start | 1, 3 |
| `move-stop.jpg` | A boy stopping on a line | 13, 15 |
| `move-arms.jpg` | Arms while running, from the front | 9, 11 |

A second file with `-bad` before the extension is optional. If it is there the
sheet shows both side by side, one marked "Like this" and one marked "Not this".
For example `shape-sit.jpg` and `shape-sit-bad.jpg`.

## Taking them

- A phone is fine. Landscape, and fill the frame with the boy.
- Photograph a coach or one boy, not the group. One person, plain background.
- Shoot the shape from the side, except the sit, the big step and the landing,
  which are shot from the front because the fault is the knees falling in.
- Get written permission from a parent before photographing any boy, and keep
  the photos in this repository only.

`.jpg` and `.png` both work. Anything over about 1600 pixels wide is trimmed
down by the build.
