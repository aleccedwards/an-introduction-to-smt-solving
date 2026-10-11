#!/usr/bin/env python3
"""Check that the student and completed notebooks stay in sync.

The two notebooks in this repo are designed as siblings: every teaching cell
(markdown and shared code) must be identical, and only the exercise/solution
cells may differ (blank or `TODO` in the student copy, filled in in the
completed copy).

Run from the repository root:

    python tools/check_sync.py

Exits non-zero if any teaching cell has drifted apart. Use it in CI or as a
pre-commit check after editing either notebook.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUDENT = ROOT / "An Introduction to SMT-solving.ipynb"
COMPLETED = ROOT / "Completed_An Introduction to SMT-solving.ipynb"

# Cell indices that are *intentionally* different between the two notebooks:
# exercise cells where the student copy is empty / a TODO scaffold and the
# completed copy holds the answer. Everything else must match exactly.
SOLUTION_CELLS = {6, 8, 10, 14, 16, 20, 21, 23}


def load(path: Path):
    with open(path) as f:
        nb = json.load(f)
    return nb["cells"]


def main() -> int:
    student = load(STUDENT)
    completed = load(COMPLETED)

    if len(student) != len(completed):
        print(f"FAIL: cell count differs ({len(student)} vs {len(completed)}).")
        return 1

    failed = False
    for i, (s_cell, c_cell) in enumerate(zip(student, completed)):
        if s_cell.get("id") != c_cell.get("id"):
            failed = True
            print(f"FAIL: cell {i} has different ids "
                  f"({s_cell.get('id')!r} vs {c_cell.get('id')!r}).")
            continue
        if i in SOLUTION_CELLS:
            continue
        s_text = "".join(s_cell["source"])
        c_text = "".join(c_cell["source"])
        if s_text != c_text:
            failed = True
            print(f"FAIL: teaching cell {i} differs between the notebooks:")
            s_lines = s_text.splitlines()
            c_lines = c_text.splitlines()
            for line in difflib_short(s_lines, c_lines):
                print("   " + line)
            print()

    if failed:
        print("The notebooks have drifted apart. Edit BOTH copies (or run the")
        print("reconciliation) and re-check.")
        return 1
    print(f"OK: all teaching cells match ({len(student)} cells checked).")
    return 0


def difflib_short(a, b):
    import difflib

    out = []
    for line in difflib.unified_diff(a, b, lineterm="", n=1):
        if line.startswith(("---", "+++", "@@")):
            continue
        out.append(line[:220])
        if len(out) > 12:
            out.append("... (diff truncated)")
            break
    return out


if __name__ == "__main__":
    sys.exit(main())