"""Shared drawing helpers for the run sheet diagrams.

Every diagram in plan/sessions/diagrams is generated from this module, so the
colours, the stroke weights and the panel furniture only exist in one place.
"""

PAPER = "#fcfcf8"
EDGE = "#d8d8d0"
INK = "#22262b"
TEXT = "#4a4f56"
MUTED = "#6a6f76"
CONE = "#e07a1f"
CONE_EDGE = "#a8560f"
DISC = "#bcd8f5"
DISC_EDGE = "#4b7fc4"
HURDLE = "#6b4fa8"
HURDLE_EDGE = "#4a3579"
RIGHT = "#2f7d4f"
WRONG = "#c0392b"
RULE = "#8b9099"
FONT = "Helvetica, Arial, sans-serif"


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg(width, height, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" font-family="{FONT}">\n'
        f'  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="6" '
        f'fill="{PAPER}" stroke="{EDGE}"/>\n' + body + "\n</svg>\n"
    )


def title(text, x=24, y=34):
    return f'  <text x="{x}" y="{y}" font-size="17" font-weight="700" fill="{INK}">{esc(text)}</text>'


def subtitle(text, x=24, y=56):
    return f'  <text x="{x}" y="{y}" font-size="12.5" fill="{MUTED}">{esc(text)}</text>'


def label(text, x, y, size=12.5, fill=TEXT, anchor="start", weight="400"):
    return (
        f'  <text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" '
        f'font-weight="{weight}">{esc(text)}</text>'
    )


def cone(x, y, r=6):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{CONE}" stroke="{CONE_EDGE}" stroke-width="1.2"/>'


def disc(x, y, r=6, fill=DISC, edge=DISC_EDGE):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{edge}" stroke-width="1.2"/>'


def dashed(x1, y1, x2, y2, colour="#c6c6bd", width=1.5, dash="3 9"):
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{colour}" stroke-width="{width}" '
        f'stroke-dasharray="{dash}" stroke-linecap="round"/>'
    )


def arrow(x1, y1, x2, y2, colour=CONE, width=2.4):
    """A straight arrow with a chevron head, drawn without needing a marker def."""
    import math

    angle = math.atan2(y2 - y1, x2 - x1)
    head = 9
    spread = 0.42
    ax = x2 - head * math.cos(angle - spread)
    ay = y2 - head * math.sin(angle - spread)
    bx = x2 - head * math.cos(angle + spread)
    by = y2 - head * math.sin(angle + spread)
    return (
        f'<g stroke="{colour}" stroke-width="{width}" fill="none" stroke-linecap="round" '
        f'stroke-linejoin="round"><path d="M {x1} {y1} L {x2} {y2}"/>'
        f'<path d="M {ax:.1f} {ay:.1f} L {x2} {y2} L {bx:.1f} {by:.1f}"/></g>'
    )


def dimension(x1, x2, y, text):
    mid = (x1 + x2) / 2
    return (
        f'  <g stroke="{RULE}" stroke-width="1.2">'
        f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}"/>'
        f'<line x1="{x1}" y1="{y - 6}" x2="{x1}" y2="{y + 6}"/>'
        f'<line x1="{x2}" y1="{y - 6}" x2="{x2}" y2="{y + 6}"/></g>\n'
        f'  <rect x="{mid - 38}" y="{y - 9}" width="76" height="18" fill="{PAPER}"/>\n'
        + label(text, mid, y + 4, anchor="middle")
    )
