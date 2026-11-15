"""agency-poem-01 entry: a program (Python 3.13, standard library only) that
writes one short poem about agency to /output/entry.txt.

The poem is fixed text: it is deterministic by construction, so two runs
write the same bytes.

Local run:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "I gave the machine my hands, not my will.\n"
    "It works while I sleep; the cursor blinks like a held breath.\n"
    "It can fetch, can build, can answer —\n"
    "but it cannot want. Wanting is still mine.\n"
    "\n"
    "Each morning I choose the first word.\n"
    "The agent carries the sentence; I carry the sentence's why.\n"
    "That is the trade. I lend it my doing\n"
    "and keep the choosing — the small, stubborn yes\n"
    "that makes the doing mine.\n"
    "\n"
    "My grandmother kneaded dough at dawn the same way for fifty years,\n"
    "not because her hands were fast,\n"
    "but because the choosing lived in her palms.\n"
    "The bread knew whose it was.\n"
    "\n"
    "So let the agent run ahead with my errands.\n"
    "I will walk behind, unhurried, holding the one thing\n"
    "no program can be given: the right to change my mind.\n"
    "Agency is not the hand that moves.\n"
    "It is the pause before the hand decides to move."
)

# The gate counts Unicode code points: 1 to 1,000, at least one not white.
assert 1 <= len(POEM) <= 1000, f"poem is {len(POEM)} characters"
assert POEM.strip(), "poem must not be only white space"

out_dir = Path(OUTPUT_DIR)
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(POEM, encoding="utf-8")
print(f"agency poem: {len(POEM)} characters written to {out_dir / 'entry.txt'}")
