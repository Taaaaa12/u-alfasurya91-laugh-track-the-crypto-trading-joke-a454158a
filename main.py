#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes a single one-line joke about crypto/trading life to /output/entry.txt.
Deterministic: the same joke every run, no network, no randomness, no input.
"""

import os

JOKE = (
    "I bought the dip, and the dip bought a shovel \u2014 "
    "now I'm a long-term investor in a coin I meant to flip by Friday."
)


def main() -> None:
    text = JOKE
    # Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
    assert 1 <= len(text) <= 200, "joke must be 1-200 characters"
    assert text.strip(), "joke must not be only whitespace"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
