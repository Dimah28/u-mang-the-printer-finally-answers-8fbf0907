"""Printer's reply: one deadpan status line, same bytes every run."""

import os

REPORT = (
    "STATUS: JAMMED. Sheets fed: 41,208. Sheets you loaded straight: 0. "
    "Thumps received: 47. Diagnosis: error 0xE3 is human."
)
MAX_CHARS = 240


def die(why):
    raise SystemExit(why)


def shape_ok(text):
    if "\n" in text or "\r" in text:
        die("entry must be a single line")
    if len(text) > MAX_CHARS:
        die("entry is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    return text


def clean(raw):
    stripped = raw.strip()
    if not stripped:
        die("entry is empty or only whitespace")
    return shape_ok(stripped)


def run():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(clean(REPORT) + "\n")


if __name__ == "__main__":
    run()
