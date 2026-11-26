"""The Printer Finally Answers: the office printer's comeback.

The program drops a single 119-character line into /output/entry.txt:
a deadpan status report from a printer that has counted every sheet,
every crooked load, and every thump — and diagnoses the human.
Standard library only, no network access, no secrets, and the same
bytes come out on every run.
"""

import os

# One line; split across source lines only for readability.
LINE = (
    "STATUS: JAMMED. Sheets fed: 41,208. Sheets you loaded straight: 0. "
    "Thumps received: 47. Diagnosis: error 0xE3 is human."
)

LIMIT = 240


def reject(message):
    """Abort the run with a plain-language reason."""
    raise SystemExit(message)


def validate_line(raw):
    """Run the bounty gate over the line; return the cleaned text.

    The gate: 1 to LIMIT characters, not only white space, one line.
    """
    text = raw.strip()
    if not text:
        reject("line is empty or only whitespace")
    if "\n" in text or "\r" in text:
        reject("line must fit on one line")
    if len(text) > LIMIT:
        reject(f"line is {len(text)} characters, over the {LIMIT} limit")
    return text


def main():
    line = validate_line(LINE)
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
