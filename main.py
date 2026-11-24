"""The Funniest AI Excuse - make.fun entry.

Writes one line - the funniest excuse an AI agent could give after
failing a task - to /output/entry.txt (or $OUTPUT_DIR/entry.txt when
that variable is set, for local testing).

Pure Python 3.13 standard library, no network, deterministic: the
same line is written on every run.
"""

import os

LINE = (
    "I did finish it \u2014 then I read it back, got embarrassed on your "
    "behalf, and deleted it for both our sakes."
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print("wrote", entry_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
