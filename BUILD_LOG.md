# Build log — agency-poem-01

## What was built (authored in this session; the starter was read only)
- `main.py` — Python 3.13, standard library only. Writes one fixed poem about
  agency to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
- The poem (807 Unicode characters): "I gave the machine my hands, not my
  will." — an agent that works while its person sleeps, the trade of lending
  the doing while keeping the choosing, a grandmother whose choosing lived in
  her palms, and the close: agency is not the hand that moves, it is the pause
  before the hand decides to move. Written for the judge's criteria in order:
  plainly about agency (handing over action, keeping choice); a felt turn
  (hands → palms → pause); the insight that wanting cannot be delegated;
  concrete words and line breaks serving the meaning; its own images.

## Local tests (2026-11-15)
- `MAKEFUN_OUTPUT_DIR=out1 python3 main.py` and a second run into out2:
  byte-identical (`diff` clean) — deterministic.
- Gate: 807 characters (1–1,000), non-whitespace present, UTF-8.
