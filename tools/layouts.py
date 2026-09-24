"""Pitch layout diagrams for the run sheets.

Four new layouts join the four already in plan/sessions/diagrams: a loop for
continuous running, a shuttle grid, an open box of scattered discs, and a
pair of gates for the sprint challenge.
"""

import math
import random

import svgkit as k

COLOURS = [("#e8807c", "#b3413c"), ("#bcd8f5", "#4b7fc4"),
           ("#f0d987", "#b8912a"), ("#a9d9ba", "#3f8459")]


def loop_grid():
    """A continuous circuit. Nobody queues and nobody stops."""
    parts = [
        k.title("One loop, about 70 metres round"),
        k.subtitle("everybody runs the same way at the same time, and nobody stops"),
    ]
    x1, y1, x2, y2 = 118, 92, 626, 288
    parts.append(f'  <rect x="{x1}" y="{y1}" width="{x2 - x1}" height="{y2 - y1}" rx="70" '
                 f'fill="none" stroke="#c6c6bd" stroke-width="1.5" stroke-dasharray="3 9"/>')
    for cx, cy in [(x1, 190), (x2, 190), (250, y1), (400, y1), (250, y2), (400, y2),
                   (150, 112), (594, 112), (150, 268), (594, 268)]:
        parts.append("  " + k.cone(cx, cy))
    parts.append("  " + k.arrow(300, y1 - 14, 360, y1 - 14))
    parts.append("  " + k.arrow(360, y2 + 14, 300, y2 + 14))
    parts.append("  " + k.arrow(x2 + 16, 160, x2 + 16, 220))
    parts.append("  " + k.arrow(x1 - 16, 220, x1 - 16, 160))
    parts.append(k.label("Slower boys run the inside of the corners.", 372, 176,
                         13, k.TEXT, "middle"))
    parts.append(k.label("Nobody laps anybody. Keep the line moving.", 372, 200,
                         13, k.TEXT, "middle"))
    parts.append(k.dimension(x1, x2, 330, "about 25 metres"))
    return k.svg(744, 356, "\n".join(parts))


def chase_ring():
    """A small ring for a pairs chase game. Round the outside, not through the middle."""
    parts = [
        k.title("A small ring, about 8 metres across"),
        k.subtitle("pairs face off, one chases the other round the outside"),
    ]
    cx, cy, r = 300, 190, 108
    parts.append(f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#c6c6bd" '
                 f'stroke-width="1.5" stroke-dasharray="3 9"/>')
    for i in range(4):
        angle = math.pi / 2 * i + math.pi / 4
        parts.append("  " + k.cone(cx + r * math.cos(angle), cy + r * math.sin(angle)))
    runner = (cx + r * math.cos(math.radians(-95)), cy + r * math.sin(math.radians(-95)))
    chaser = (cx + r * math.cos(math.radians(-125)), cy + r * math.sin(math.radians(-125)))
    parts.append("  " + k.disc(*runner, 7, k.RIGHT, k.RIGHT))
    parts.append(k.label("runner", runner[0], runner[1] - 14, 12.5, k.TEXT, "middle"))
    parts.append("  " + k.disc(*chaser, 7, k.WRONG, k.WRONG))
    parts.append(k.label("chaser", chaser[0] - 8, chaser[1] - 10, 12.5, k.TEXT, "end"))
    ax1 = (cx + r * math.cos(math.radians(-70)), cy + r * math.sin(math.radians(-70)))
    ax2 = (cx + r * math.cos(math.radians(-40)), cy + r * math.sin(math.radians(-40)))
    parts.append("  " + k.arrow(*ax1, *ax2))
    parts.append(k.label('Both run round the ring. Call "switch" to swap them.', cx, cy + r + 40,
                         13, k.TEXT, "middle"))
    return k.svg(600, 372, "\n".join(parts))


def shuttle_weave():
    """A shuttle circuit: sprint, tight turn, weave, final cut, sprint out."""
    parts = [
        k.title("Sprint, turn, weave, cut, sprint out"),
        k.subtitle("one at a time, full rest before the next boy goes"),
    ]
    start = (90, 300)
    turn = (260, 130)
    weave = [(380, 250), (450, 170)]
    cut = (580, 260)
    finish = (680, 130)

    parts.append("  " + k.disc(*start, 7))
    parts.append(k.label("start", start[0], start[1] + 24, 12.5, k.TEXT, "middle"))
    parts.append("  " + k.arrow(start[0] + 20, start[1] - 16, turn[0] - 18, turn[1] + 18))

    parts.append("  " + k.cone(*turn))
    parts.append(k.label("plant and turn tight", turn[0], turn[1] - 16, 12.5, k.TEXT, "middle"))
    parts.append("  " + k.arrow(turn[0] + 16, turn[1] + 12, weave[0][0] - 18, weave[0][1] - 12))

    for wx, wy in weave:
        parts.append("  " + k.cone(wx, wy))
    parts.append(k.label("weave: short, choppy steps", (weave[0][0] + weave[1][0]) / 2, weave[0][1] + 26,
                         12.5, k.TEXT, "middle"))
    parts.append("  " + k.arrow(weave[0][0] + 16, weave[0][1] - 8, weave[1][0] - 16, weave[1][1] + 8))
    parts.append("  " + k.arrow(weave[1][0] + 16, weave[1][1] + 10, cut[0] - 18, cut[1] - 10))

    parts.append("  " + k.cone(*cut))
    parts.append(k.label("cut hard round this one", cut[0], cut[1] + 24, 12.5, k.TEXT, "middle"))
    parts.append("  " + k.arrow(cut[0] + 8, cut[1] - 20, finish[0] - 12, finish[1] + 20))

    parts.append("  " + k.disc(*finish, 7, k.RIGHT, k.RIGHT))
    parts.append(k.label("finish", finish[0], finish[1] - 16, 12.5, k.TEXT, "middle"))

    parts.append(k.label("Walk back. Full rest before the next go.", 372, 340, 13, k.MUTED, "middle"))
    return k.svg(744, 360, "\n".join(parts))


def shuttle_grid():
    """Six lanes with a turn cone at 5, 10 and 15 metres."""
    parts = [
        k.title("Six lanes, turn cones at 5, 10 and 15 metres"),
        k.subtitle("out to the called cone, touch it, and back"),
    ]
    xs = [118, 280, 442, 604]
    for row in range(6):
        y = 94 + row * 30
        parts.append("  " + k.dashed(xs[0], y, xs[-1], y))
        for x in xs:
            parts.append("  " + k.cone(x, y))
        parts.append(k.label(str(row + 1), 98, y + 4, 12, k.MUTED, "end"))
    parts.append(k.label("start", xs[0], 82, 12.5, k.TEXT, "middle"))
    for x, name in zip(xs[1:], ("5 m", "10 m", "15 m")):
        parts.append(k.label(name, x, 82, 12.5, k.TEXT, "middle"))
    parts.append("  " + k.arrow(140, 292, 258, 292))
    parts.append("  " + k.arrow(258, 312, 140, 312))
    parts.append(k.label("out on the shout, back at the same speed", 300, 316, 13, k.TEXT))
    return k.svg(744, 344, "\n".join(parts))


def scatter_box():
    """An open box of scattered discs."""
    rng = random.Random(11)
    parts = [
        k.title("The open box, a disc each, four colours"),
        k.subtitle("about 20 by 20 metres for 25 boys, no lanes and no queue"),
    ]
    parts.append(f'  <rect x="118" y="86" width="508" height="216" rx="4" fill="none" '
                 f'stroke="{k.RULE}" stroke-width="1.6"/>')
    for corner in [(118, 86), (626, 86), (118, 302), (626, 302)]:
        parts.append("  " + k.cone(*corner, r=7))
    placed = []
    for _ in range(25):
        for _ in range(200):
            x = rng.randint(140, 604)
            y = rng.randint(106, 282)
            if all((x - px) ** 2 + (y - py) ** 2 > 1300 for px, py in placed):
                placed.append((x, y))
                break
    for index, (x, y) in enumerate(placed):
        fill, edge = COLOURS[index % 4]
        parts.append("  " + k.disc(x, y, 6, fill, edge))
    parts.append(k.label("a disc for every boy", 118, 326, 13, k.TEXT))
    parts.append(k.label("cone at each corner", 400, 326, 13, k.TEXT))
    return k.svg(744, 344, "\n".join(parts))


def two_gates():
    """A start, a coach in the middle, and a gate to run through at either side."""
    parts = [
        k.title("Two gates, 12 metres away"),
        k.subtitle("he does not know which gate until he is running"),
    ]
    parts.append("  " + k.dashed(140, 94, 140, 300, k.RULE, 1.6, "6 6"))
    parts.append(k.label("start", 140, 82, 12.5, k.TEXT, "middle"))
    for y in (110, 146, 182, 218, 254, 290):
        parts.append("  " + k.disc(140, y, 6))
    for gy in (118, 158):
        parts.append("  " + k.cone(560, gy, r=7))
    for gy in (250, 290):
        parts.append("  " + k.cone(560, gy, r=7))
    parts.append(f'  <line x1="560" y1="118" x2="560" y2="158" stroke="{k.CONE}" '
                 f'stroke-width="1.6" stroke-dasharray="4 4"/>')
    parts.append(f'  <line x1="560" y1="250" x2="560" y2="290" stroke="{k.CONE}" '
                 f'stroke-width="1.6" stroke-dasharray="4 4"/>')
    parts.append(k.label("gate 1", 596, 142, 13, k.TEXT))
    parts.append(k.label("gate 2", 596, 274, 13, k.TEXT))
    parts.append("  " + k.arrow(170, 196, 530, 142))
    parts.append("  " + k.arrow(170, 200, 530, 266))
    parts.append(f'  <circle cx="352" cy="204" r="11" fill="{k.PAPER}" stroke="{k.HURDLE}" '
                 f'stroke-width="2.6"/>')
    parts.append(k.label("coach calls the gate", 372, 209, 13, k.HURDLE, "start", "700"))
    parts.append(k.dimension(140, 560, 328, "12 metres"))
    return k.svg(744, 352, "\n".join(parts))


def pace_gauge():
    """The only endurance rule a coach needs: can the boy still talk?"""
    bands = [("walking", "#e8eae7"), ("talking pace", "#a9d9ba"),
             ("puffing", "#f0d987"), ("all out", "#e8807c")]
    parts = [
        k.title("Talking pace, and how to check it"),
        k.subtitle("run beside a boy and ask him his name and his club"),
    ]
    x = 118
    width = 127
    for name, fill in bands:
        parts.append(f'  <rect x="{x}" y="86" width="{width}" height="54" fill="{fill}" '
                     f'stroke="{k.EDGE}"/>')
        parts.append(k.label(name, x + width / 2, 118, 13.5, k.INK, "middle", "700"))
        x += width
    parts.append(f'  <rect x="245" y="86" width="127" height="54" fill="none" '
                 f'stroke="{k.RIGHT}" stroke-width="3"/>')
    parts.append("  " + k.arrow(308, 176, 308, 148, k.RIGHT, 2.6))
    parts.append(k.label("Every endurance night lives in this band.", 308, 200, 14,
                         k.INK, "middle", "700"))
    lines = [
        'He answers in a full sentence: he is too easy. Tell him to push on.',
        'He answers in short words: that is the band. Leave him alone.',
        'He cannot answer: he is too hard. Tell him to ease off, do not stop him.',
    ]
    for index, text in enumerate(lines):
        parts.append(k.label(text, 118, 232 + index * 24, 13.5, k.TEXT))
    return k.svg(744, 320, "\n".join(parts))


def staggered_lanes():
    """Six lanes extended to 30m with staggered start cones for passing down the line."""
    parts = [
        k.title("Six lanes, 30 metres with staggered start"),
        k.subtitle("left cone 3m up, each cone to the right 0.5m back"),
    ]
    finish_x = 608
    start_xs = [170, 158, 146, 134, 122, 110]
    ys = [74, 100, 126, 152, 178, 204]

    for sx, y in zip(start_xs, ys):
        parts.append(f'  <line x1="{sx + 10}" y1="{y}" x2="{finish_x - 10}" y2="{y}" '
                     f'stroke="#c6c6bd" stroke-width="1.5" stroke-dasharray="3 9" stroke-linecap="round"/>')

    for sx, y in zip(start_xs, ys):
        parts.append("  " + k.cone(sx, y, r=6))
        parts.append("  " + k.cone(finish_x, y, r=6))

    for i, (sx, y) in enumerate(zip(start_xs, ys), start=1):
        parts.append(f'  <text x="{sx - 16}" y="{y + 4}" font-size="12" fill="{k.MUTED}" text-anchor="end">{i}</text>')

    parts.append(k.label("staggered start", 140, 56, 12.5, k.TEXT, "middle"))
    parts.append(k.label("finish", finish_x, 56, 12.5, k.TEXT, "middle"))

    parts.append("  " + k.arrow(174, 82, 120, 200, k.CONE, 2.0))
    parts.append(k.label("ball passes down the line", 190, 140, 12, k.CONE, "start", "700"))

    parts.append(k.dimension(110, finish_x, 232, "30 metres"))

    parts.append('  <g fill="#8b9099" font-size="11.5"><circle cx="656" cy="254" r="6" '
                 f'fill="{k.CONE}" stroke="{k.CONE_EDGE}" stroke-width="1.2"/><text x="670" y="258">cone</text></g>')

    return k.svg(760, 276, "\n".join(parts))


BUILDERS = {
    "move-pace": pace_gauge,
    "loop-grid": loop_grid,
    "chase-ring": chase_ring,
    "shuttle-weave": shuttle_weave,
    "shuttle-grid": shuttle_grid,
    "scatter-box": scatter_box,
    "two-gates": two_gates,
    "staggered-lanes": staggered_lanes,
}


def build(out_dir):
    for name, fn in BUILDERS.items():
        with open(f"{out_dir}/{name}.svg", "w") as handle:
            handle.write(fn())
    return list(BUILDERS)
