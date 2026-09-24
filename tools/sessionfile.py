"""Read one session markdown file into the shape build_sheets.py renders.

A session file has three parts, in order: a header block the build owns, a
--- frontmatter block plus body a coach owns, and a link-row block the build
owns. See design/ADR-001-markdown-session-sources.md for the format.

Every function here reports faults instead of raising, so build_sheets.py can
collect every fault across all 20 files before it writes anything.
"""

import re

HEADER_OPEN = "<!-- built: header -->"
HEADER_CLOSE = "<!-- /built -->"
LINKS_OPEN = "<!-- built: links -->"
LINKS_CLOSE = "<!-- /built -->"

REQUIRED_KEYS = ("n", "date", "theme", "code", "match", "kit", "coach", "wet")

IMAGE_RE = re.compile(r'^!\[(?P<alt>[^\]]*)\]\((?P<src>[^)]+)\)$')
PART_RE = re.compile(r'^###\s+(?P<time>[^·]+)·(?P<kind>[^·]+)·(?P<name>.+)$')


def split_marked_regions(text, path):
    """Return (middle_text, errors). middle_text is the frontmatter + body,
    the part between the header block and the link-row block, unchanged."""
    errors = []
    h_start = text.find(HEADER_OPEN)
    if h_start == -1:
        return None, [f"{path}: missing '{HEADER_OPEN}' marker"]
    h_close = text.find(HEADER_CLOSE, h_start + len(HEADER_OPEN))
    if h_close == -1:
        return None, [f"{path}: '{HEADER_OPEN}' is never closed"]
    after_header = h_close + len(HEADER_CLOSE)
    l_start = text.find(LINKS_OPEN, after_header)
    if l_start == -1:
        return None, [f"{path}: missing '{LINKS_OPEN}' marker"]
    l_close = text.find(LINKS_CLOSE, l_start + len(LINKS_OPEN))
    if l_close == -1:
        return None, [f"{path}: '{LINKS_OPEN}' is never closed"]
    middle = text[after_header:l_start].strip("\n")
    return middle, errors


def parse_frontmatter(text, path):
    """Split a --- fenced block of key: value lines and - item lists from the
    body under it. Returns (data, body_text, errors)."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text, [f"{path}: the file must open with a --- frontmatter block"]
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, "", [f"{path}: the --- frontmatter block is never closed"]

    data = {}
    errors = []
    i = 1
    while i < end:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("  -") or line.startswith("-"):
            errors.append(f"{path}: list item with no key above it: {line.strip()!r}")
            i += 1
            continue
        if ":" not in line:
            errors.append(f"{path}: frontmatter line is not 'key: value': {line!r}")
            i += 1
            continue
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = rest.strip()
        if rest:
            data[key] = rest
            i += 1
        else:
            items = []
            i += 1
            while i < end and lines[i].strip().startswith("-"):
                items.append(lines[i].strip()[1:].strip())
                i += 1
            data[key] = items

    body = "\n".join(lines[end + 1:]).strip("\n")
    return data, body, errors


def parse_body(body_text, path):
    """Split the body into the setup context, setup pictures, the exercises
    under '## The station', and the bullets under '## Coach one
    thing'. Returns (parsed, errors)."""
    errors = []
    context_lines = []
    images = []
    parts = []
    watch = []
    section = "intro"
    current = None

    def close_part():
        nonlocal current
        if current is not None:
            parts.append(current)
            current = None

    for raw in body_text.split("\n"):
        line = raw.strip()
        if not line:
            continue

        if line.startswith("### "):
            if section != "minutes":
                errors.append(f"{path}: a ### heading outside "
                               f"'## The station': {line!r}")
                continue
            match = PART_RE.match(line)
            if not match:
                errors.append(f"{path}: exercise heading must read "
                               f"'time · kind · name': {line!r}")
                continue
            close_part()
            current = {
                "time": match.group("time").strip(),
                "kind": match.group("kind").strip(),
                "name": match.group("name").strip(),
                "lines": [],
            }
            continue

        if line.startswith("## "):
            close_part()
            heading = line[3:].strip()
            if heading == "The station":
                section = "minutes"
            elif heading == "Coach one thing":
                section = "coach"
            else:
                errors.append(f"{path}: unknown section heading: {line!r}")
                section = "unknown"
            continue

        image = IMAGE_RE.match(line)
        if image:
            if section == "intro":
                images.append((image.group("alt"), image.group("src")))
            else:
                errors.append(f"{path}: image is not in the setup section: {line!r}")
            continue

        if line.startswith("- "):
            item = line[2:].strip()
            if current is not None:
                current["lines"].append(item)
            elif section == "coach":
                watch.append(item)
            else:
                errors.append(f"{path}: bullet with no exercise or coach card above it: {line!r}")
            continue

        if section == "intro":
            context_lines.append(line)
        else:
            errors.append(f"{path}: text that is not a heading, bullet or picture: {line!r}")

    close_part()

    if not parts:
        errors.append(f"{path}: no exercises found under '## The station'")
    elif len(parts) != 2:
        errors.append(f"{path}: expected exactly 2 exercises under '## The station', found {len(parts)}")
    else:
        if parts[0]["time"] != "1 to 6":
            errors.append(f"{path}: first exercise time must be '1 to 6', not {parts[0]['time']!r}")
        if parts[1]["time"] != "6 to 11":
            errors.append(f"{path}: second exercise time must be '6 to 11', not {parts[1]['time']!r}")

    for p in parts:
        if "wake up" in p["kind"].lower() or "wake up" in p["name"].lower():
            errors.append(f"{path}: wake up games are no longer used: {p['name']!r}")

    if section == "intro":
        errors.append(f"{path}: no '## The station' heading found")

    return {
        "context": " ".join(context_lines).strip(),
        "images": images,
        "parts": parts,
        "watch": watch,
    }, errors


def check_required_keys(data, path):
    errors = [f"{path}: missing frontmatter key '{key}'"
              for key in REQUIRED_KEYS if key not in data]
    if "night" not in data and "kind" not in data:
        errors.append(f"{path}: set frontmatter key 'night' (push or ease) or 'kind' "
                       "(a custom one-line description) to say what kind of night it is")
    if "night" in data and data["night"] not in ("push", "ease"):
        errors.append(f"{path}: frontmatter key 'night' must be 'push' or 'ease', "
                       f"not {data['night']!r}")
    if "kit" in data and not isinstance(data["kit"], list):
        errors.append(f"{path}: frontmatter key 'kit' must be a list of '-' items")
    return errors


def parse_session_file(text, path):
    """Parse one full session file. Returns (session_dict_or_None, errors, images).

    images is the list of (alt, src) pictures found in the setup section, and
    is returned even when other faults make `session` None, so a caller can
    still check every image path exists rather than stopping at the first
    kind of fault this file has.
    """
    middle, errors = split_marked_regions(text, path)
    if middle is None:
        return None, errors, []

    data, body_text, fm_errors = parse_frontmatter(middle, path)
    errors += fm_errors
    errors += check_required_keys(data, path)

    body, body_errors = parse_body(body_text, path)
    errors += body_errors
    images = body["images"]

    if errors:
        return None, errors, images

    try:
        n = int(data["n"])
    except ValueError:
        return None, [f"{path}: frontmatter key 'n' must be a number, not {data['n']!r}"], images

    session = {
        "n": n,
        "date": data["date"],
        "theme": data["theme"],
        "code": data["code"],
        "match": data["match"],
        "kit": data["kit"],
        "coach": data["coach"],
        "wet": data["wet"],
        "kind": data.get("kind"),
        "night": data.get("night"),
        "line": body["context"],
        "images": body["images"],
        "parts": [(p["time"], p["kind"], p["name"], p["lines"]) for p in body["parts"]],
        "watch": body["watch"],
    }
    return session, [], images
