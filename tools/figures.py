"""Right and wrong stick figure panels for the run sheets.

A coach who has never taught athletic development gets one picture per idea:
the shape done well beside the same shape done badly, with the fault named.
Each pose is a head circle plus a list of polylines, so a pose is data and the
drawing code is written once.
"""

import svgkit as k

CELL_W = 296
CELL_H = 250
GROUND = 232
LIMB = 4.2

# Each pose: head (x, y, r), lines (polylines through the joints), extras (raw svg).
POSES = {
    "sit-good": {
        "head": (120, 96, 15),
        "lines": [
            [(120, 111), (120, 178)],
            [(96, 124), (144, 124)],
            [(102, 178), (80, 206), (96, GROUND)],
            [(138, 178), (160, 206), (144, GROUND)],
            [(96, 124), (76, 146), (86, 168)],
            [(144, 124), (164, 146), (154, 168)],
        ],
        "extras": [
            k.dashed(96, 204, 96, GROUND, k.RIGHT, 1.6, "4 4"),
            k.dashed(144, 204, 144, GROUND, k.RIGHT, 1.6, "4 4"),
        ],
    },
    "sit-bad": {
        "head": (120, 96, 15),
        "lines": [
            [(120, 111), (120, 178)],
            [(96, 124), (144, 124)],
            [(102, 178), (116, 206), (96, GROUND)],
            [(138, 178), (124, 206), (144, GROUND)],
            [(96, 124), (76, 146), (86, 168)],
            [(144, 124), (164, 146), (154, 168)],
        ],
        "extras": [
            k.dashed(96, 204, 96, GROUND, k.WRONG, 1.6, "4 4"),
            k.dashed(144, 204, 144, GROUND, k.WRONG, 1.6, "4 4"),
        ],
    },
    "landing-good": {
        "head": (120, 66, 15),
        "lines": [
            [(120, 81), (120, 150)],
            [(94, 94), (146, 94)],
            [(102, 150), (94, 189), (96, GROUND)],
            [(138, 150), (146, 189), (144, GROUND)],
            [(94, 94), (78, 120), (74, 148)],
            [(146, 94), (162, 120), (166, 148)],
        ],
        "extras": [],
    },
    "landing-bad": {
        "head": (120, 48, 15),
        "lines": [
            [(120, 63), (120, 140)],
            [(94, 76), (146, 76)],
            [(102, 140), (114, 186), (98, GROUND)],
            [(138, 140), (126, 186), (142, GROUND)],
            [(94, 76), (84, 112), (82, 146)],
            [(146, 76), (156, 112), (158, 146)],
        ],
        "extras": [
            k.label("THUMP", 120, GROUND + 22, 12, k.WRONG, "middle", "700"),
        ],
    },
    "bigstep-good": {
        "head": (108, 52, 15),
        "lines": [
            [(108, 67), (108, 162)],
            [(84, 80), (132, 80)],
            [(98, 162), (74, 200), (72, GROUND)],
            [(84, 80), (70, 114), (66, 148)],
            [(132, 80), (146, 114), (150, 148)],
        ],
        "back_leg": [(126, 162), (160, 214), (176, 228)],
        "extras": [k.dashed(72, 198, 72, GROUND, k.RIGHT, 1.6, "4 4")],
    },
    "bigstep-bad": {
        "head": (108, 52, 15),
        "lines": [
            [(108, 67), (108, 162)],
            [(84, 80), (132, 80)],
            [(98, 162), (108, 200), (72, GROUND)],
            [(84, 80), (70, 114), (66, 148)],
            [(132, 80), (146, 114), (150, 148)],
        ],
        "back_leg": [(126, 162), (160, 214), (176, 228)],
        "extras": [k.dashed(72, 198, 72, GROUND, k.WRONG, 1.6, "4 4")],
    },
    "arms-good": {
        "head": (120, 44, 15),
        "lines": [
            [(120, 59), (120, 140)],
            [(94, 72), (146, 72)],
            [(102, 140), (100, 184), (98, GROUND)],
            [(138, 140), (140, 184), (142, GROUND)],
            [(94, 72), (82, 106), (92, 82)],
            [(146, 72), (158, 108), (152, 142)],
        ],
        "extras": [k.dashed(120, 30, 120, GROUND, "#c6c6bd", 1.4, "5 6")],
    },
    "arms-bad": {
        "head": (120, 44, 15),
        "lines": [
            [(120, 59), (120, 140)],
            [(94, 72), (146, 72)],
            [(102, 140), (100, 184), (98, GROUND)],
            [(138, 140), (140, 184), (142, GROUND)],
            [(94, 72), (98, 108), (142, 92)],
            [(146, 72), (142, 118), (100, 134)],
        ],
        "extras": [k.dashed(120, 30, 120, GROUND, "#c6c6bd", 1.4, "5 6")],
    },
    "bow-good": {
        "head": (66, 100, 14),
        "lines": [
            [(78, 106), (152, 132)],
            [(152, 132), (158, 178), (150, GROUND)],
            [(138, GROUND), (172, GROUND)],
            [(90, 112), (98, 148), (104, 182)],
        ],
        "extras": [
            k.dashed(56, 88, 164, 126, k.RIGHT, 2.0, "6 5"),
            k.label("flat", 122, 92, 12, k.RIGHT, "middle", "700"),
        ],
    },
    "bow-bad": {
        "head": (72, 118, 14),
        "lines": [
            [(146, 134), (122, 116), (100, 106), (84, 112)],
            [(146, 134), (146, 182), (144, GROUND)],
            [(132, GROUND), (166, GROUND)],
            [(88, 118), (96, 152), (100, 186)],
        ],
        "extras": [
            k.dashed(62, 106, 158, 128, k.WRONG, 2.0, "6 5"),
            k.label("rounded", 110, 92, 12, k.WRONG, "middle", "700"),
        ],
    },
    "plank-good": {
        "shift": -34,
        "head": (44, 162, 13),
        "lines": [
            [(56, 166), (66, 170), (136, 188), (206, 206)],
            [(66, 170), (62, 216), (34, 216)],
            [(206, 206), (218, 224)],
        ],
        "extras": [k.dashed(66, 170, 206, 206, k.RIGHT, 1.8, "5 5")],
    },
    "plank-bad": {
        "shift": -34,
        "head": (44, 176, 13),
        "lines": [
            [(56, 180), (66, 184), (132, 146), (206, 206)],
            [(66, 184), (62, 216), (34, 216)],
            [(206, 206), (218, 224)],
        ],
        "extras": [
            k.dashed(66, 184, 206, 206, k.WRONG, 1.8, "5 5"),
            k.label("backside up", 132, 132, 12, k.WRONG, "middle", "700"),
        ],
    },
    "firststep-good": {
        "head": (176, 66, 14),
        "lines": [
            [(166, 76), (110, 134)],
            [(110, 134), (150, 148), (176, 178)],
            [(110, 134), (76, 178), (52, GROUND)],
            [(156, 86), (180, 108), (192, 86)],
            [(156, 86), (132, 112), (120, 142)],
        ],
        "extras": [k.arrow(196, 150, 244, 128, k.RIGHT, 2.6)],
    },
    "firststep-bad": {
        "head": (120, 54, 14),
        "lines": [
            [(120, 68), (120, 142)],
            [(120, 142), (112, 186), (108, GROUND)],
            [(120, 142), (132, 186), (136, GROUND)],
            [(120, 82), (104, 118), (100, 152)],
            [(120, 82), (136, 118), (140, 152)],
        ],
        "extras": [k.arrow(178, 90, 178, 44, k.WRONG, 2.6)],
    },
    "stop-good": {
        "head": (104, 74, 14),
        "lines": [
            [(108, 88), (130, 146)],
            [(130, 146), (120, 186), (104, GROUND)],
            [(130, 146), (152, 182), (162, GROUND)],
            [(112, 98), (96, 124), (88, 150)],
            [(112, 98), (128, 122), (138, 146)],
        ],
        "extras": [
            f'<line x1="196" y1="72" x2="196" y2="{GROUND}" stroke="{k.CONE}" stroke-width="2.4"/>',
            k.label("line", 196, 62, 12, k.CONE, "middle", "700"),
        ],
    },
    "stop-bad": {
        "head": (170, 66, 14),
        "lines": [
            [(162, 80), (128, 144)],
            [(128, 144), (124, 188), (120, GROUND)],
            [(128, 144), (140, 186), (144, GROUND)],
            [(156, 90), (176, 116), (188, 138)],
            [(156, 90), (134, 112), (126, 140)],
        ],
        "extras": [
            f'<line x1="196" y1="72" x2="196" y2="{GROUND}" stroke="{k.CONE}" stroke-width="2.4"/>',
            k.label("line", 196, 62, 12, k.CONE, "middle", "700"),
        ],
    },
}


def _draw(name, colour):
    pose = POSES[name]
    hx, hy, hr = pose["head"]
    out = [f'  <g stroke="{colour}" stroke-width="{LIMB}" fill="none" '
           f'stroke-linecap="round" stroke-linejoin="round">']
    for line in pose["lines"]:
        d = " L ".join(f"{x} {y}" for x, y in line)
        out.append(f'    <path d="M {d}"/>')
    out.append("  </g>")
    if pose.get("back_leg"):
        d = " L ".join(f"{x} {y}" for x, y in pose["back_leg"])
        out.append(f'  <path d="M {d}" stroke="{colour}" stroke-width="{LIMB}" fill="none" '
                   f'stroke-linecap="round" stroke-linejoin="round" opacity="0.42"/>')
    out.append(f'  <circle cx="{hx}" cy="{hy}" r="{hr}" fill="{k.PAPER}" stroke="{colour}" '
               f'stroke-width="{LIMB}"/>')
    out.extend("  " + e for e in pose["extras"])
    return "\n".join(out)


def _tick(x, y):
    return (f'  <g stroke="{k.RIGHT}" stroke-width="3" fill="none" stroke-linecap="round" '
            f'stroke-linejoin="round"><circle cx="{x}" cy="{y}" r="11"/>'
            f'<path d="M {x - 5} {y} L {x - 1} {y + 5} L {x + 6} {y - 5}"/></g>')


def _cross(x, y):
    return (f'  <g stroke="{k.WRONG}" stroke-width="3" fill="none" stroke-linecap="round">'
            f'<circle cx="{x}" cy="{y}" r="11"/>'
            f'<path d="M {x - 5} {y - 5} L {x + 5} {y + 5} M {x + 5} {y - 5} L {x - 5} {y + 5}"/></g>')


def panel(heading, good_pose, good_caption, bad_pose, bad_caption):
    """One diagram: the shape done right on the left, the usual fault on the right."""
    top = 48
    width = CELL_W * 2 + 24
    height = top + CELL_H + 40
    parts = [k.title(heading)]
    for index, (pose, caption, ok) in enumerate(
        ((good_pose, good_caption, True), (bad_pose, bad_caption, False))
    ):
        ox = 12 + index * (CELL_W + 12)
        colour = k.RIGHT if ok else k.WRONG
        parts.append(
            f'  <rect x="{ox}" y="{top}" width="{CELL_W}" height="{CELL_H}" rx="5" '
            f'fill="#ffffff" stroke="{k.EDGE}"/>'
        )
        parts.append(
            f'  <line x1="{ox + 16}" y1="{top + GROUND}" x2="{ox + CELL_W - 16}" '
            f'y2="{top + GROUND}" stroke="{k.RULE}" stroke-width="1.4"/>'
        )
        shift = POSES[pose].get("shift", 0)
        centre = (CELL_W - 240) / 2
        parts.append(f'  <g transform="translate({ox + centre}, {top + shift})">')
        parts.append(_draw(pose, colour))
        parts.append("  </g>")
        parts.append(_tick(ox + 24, top + 22) if ok else _cross(ox + 24, top + 22))
        parts.append(
            k.label("Like this" if ok else "Not this", ox + 44, top + 27, 13.5, colour, "start", "700")
        )
        parts.append(k.label(caption, ox + CELL_W / 2, height - 14, 13, k.TEXT, "middle"))
    return k.svg(width, height, "\n".join(parts))


PANELS = {
    "shape-sit": ("The sit", "sit-good", "Knees track out over the toes",
                  "sit-bad", "Knees fall in towards each other"),
    "shape-bow": ("The bow", "bow-good", "Back flat, the bend comes from the hips",
                  "bow-bad", "Back rounds, legs lock straight"),
    "shape-plank": ("The plank", "plank-good", "Straight from the head to the heels",
                    "plank-bad", "Backside up in the air"),
    "shape-big-step": ("The big step", "bigstep-good", "Front knee stays over the front foot",
                       "bigstep-bad", "Front knee falls in towards the middle"),
    "shape-landing": ("The landing", "landing-good", "Knees bend and stay apart, no noise",
                      "landing-bad", "Straight legs, knees touch, a thump"),
    "move-first-step": ("The first step", "firststep-good", "Body leans, the first step goes forward",
                        "firststep-bad", "Stands up tall and wastes a step"),
    "move-stop": ("Stopping on the line", "stop-good", "Sits down into the stop, chest up",
                  "stop-bad", "Stays upright and tips over the line"),
    "move-arms": ("Arms when running", "arms-good", "Hands stay on their own side of the body",
                  "arms-bad", "Hands swing across the chest"),
}


def build(out_dir):
    written = []
    for name, args in PANELS.items():
        path = f"{out_dir}/{name}.svg"
        with open(path, "w") as handle:
            handle.write(panel(*args))
        written.append(path)
    return written
