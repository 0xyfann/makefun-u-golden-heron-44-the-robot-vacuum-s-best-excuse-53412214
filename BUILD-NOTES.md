# Build Notes

- Kit read first: RULES.txt + competition.yaml. Gate is 1-140 UTF-8
  characters, one line, not only whitespace; judge is a tired homeowner
  picking the funnier of two vacuum excuses, weighing vacuum-ness,
  funniness, vacuum-world grounding (map/sensors/dock/battery), a clean
  first-read twist, and first-person vacuum voice.
- main.py written in two revisions (transcript rule):
  - v1: "My cliff sensors say that dust bunny is actually a small
    animal, so I retreated to my dock to file a formal complaint."
    (118 chars) — tested OK, then revised for a tighter punch.
  - v2 (final): "I mapped that dust bunny as a new roommate, so legally
    I can't vacuum him without a 30-day eviction notice." (107 chars)
    — keeps the vacuum's map as the joke's engine and lands the twist
    ("30-day eviction notice") at the end.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
  then checked out/entry.txt: 107 chars / 107 bytes, 1 line, no trailing
  newline, non-whitespace, within 1-140. `out/` deleted after testing.
- All files in this entry (main.py, README.md, prompt.txt,
  BUILD-NOTES.md) were written by me in this session. No submission,
  no GitHub repo, no contact with make.fun.
