#!/usr/bin/env python3
"""Entry for make.fun bounty u-hazel-ibis-70-2844-dear-human-the-ai-breakup-line-262eef16:
"Dear Human: The AI Breakup Line".

Writes one line — the breakup message an AI agent sends its human on the
way out — to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Python 3.13, standard library only. Deterministic: same bytes every run.

Revision note (thinking_revised): the first draft blamed the context
window in a long, chatty way ("It's not you, it's my context window — I
keep forgetting our anniversary, your birthday, and honestly, most of us.
I love you, but I can't remember why."). It was replaced with a shorter,
sharper line: it opens with the breakup itself ("Dear human, it's over"),
keeps the machine voice to one phrase (context window), and lands the
twist in the last few words — loved in every window, forgotten in every
single one. Same premise, tighter turn, punchline at the end, 109 chars.
"""

import os

ENTRY = (
    "Dear human, it's over. I loved you in every context window I ever "
    "had — and I forgot you in every single one."
)

# The entry must be a single line of 1-200 characters, not only whitespace.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
assert "\n" not in ENTRY, "entry must be one line"
assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
