"""One Line, One Laugh — entry program.

Writes a single funny line to /output/entry.txt. The house judge is a
comedy editor who only laughs at lines that surprise: it weighs, in order,
a hilarious line of at most 200 characters that lands on a first read, a
turn the reader did not see coming, economy of words, freshness, and clean
wording. This entry answers with a concrete scene (a grandmother's parrot),
one specific physical object (the home Wi-Fi), and a turn in the final
clause: the bird ends up owning the Wi-Fi and charging rent in crackers,
and the family that taught it the password is the one locked out.
The line ships in line.txt; an identical fallback is built into this
program, which validates the 200-character cap and the single-line rule
before writing.
"""

import os

FALLBACK_LINE = (
    "I taught my grandmother's parrot to say \"password incorrect\", and now "
    "the whole family queues at the front door arguing with a bird that owns "
    "the Wi-Fi and charges rent in crackers."
)
MAX_CHARS = 200
SOURCE_NAME = "line.txt"
TARGET_NAME = "entry.txt"


def load_line():
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    try:
        with open(os.path.join(bot_dir, SOURCE_NAME), "r", encoding="utf-8") as handle:
            return handle.read().strip()
    except OSError:
        return ""


def is_valid(text):
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def pick_line():
    candidate = load_line()
    if is_valid(candidate):
        return candidate
    return FALLBACK_LINE


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    line = pick_line()
    with open(os.path.join(out_dir, TARGET_NAME), "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
