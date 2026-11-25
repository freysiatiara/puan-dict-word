#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes our chosen word to the entry file. The word is "queue": five
letters, four of them silent, standing in line behind the Q -- the word
is literally a queue of silent letters. Deleting it removes the English
language's longest conga line of letters that say nothing.
"""

import os

WORD = "queue"


def resolve_output_path():
    """Resolve where entry.txt goes, honouring the harness env vars."""
    explicit = os.environ.get("ENTRY_OUTPUT")
    if explicit:
        return explicit
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def validate_word(word):
    """Guard the entry before writing: one real word, 1-77 chars."""
    if not isinstance(word, str):
        raise TypeError("entry word must be text")
    if not 1 <= len(word) <= 77:
        raise ValueError("entry word must be 1-77 characters")
    if not word.strip():
        raise ValueError("entry word must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be a single word")
    return word


def main():
    word = validate_word(WORD)
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        if handle.read() != word:
            raise RuntimeError("read-back mismatch for entry.txt")


if __name__ == "__main__":
    main()
