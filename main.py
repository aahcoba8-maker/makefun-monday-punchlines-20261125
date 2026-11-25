"""Monday Morning Punchlines — one joke about Monday mornings."""
import os

TEXT = "Monday morning showed up an hour early just to watch me panic. It brought popcorn."


def main():
    # Self-gate mirroring the sealed scorer: UTF-8 text, 1-200 chars,
    # single line, not only whitespace.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert "\n" not in TEXT and TEXT.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(TEXT)


if __name__ == "__main__":
    main()
