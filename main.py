"""Have You Tried Turning It Off? — make.fun one-liner entry.

Writes a single line of tech-support dialogue to entry.txt:
a cheerful, useless support agent's reply to a desperate customer,
twisting the classic "turn it off and on again" cliche.
"""

import os

LINE = "Have you tried turning it off and on again? Great — now do it slower, so I can pretend there's a step two."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
