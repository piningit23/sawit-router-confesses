#!/usr/bin/env python3
"""The Router Confesses - make.fun entry.

Writes one line to /output/entry.txt: a home Wi-Fi router's excuse
for dropping the connection at the exact climax of a movie.
"""

import os

ENTRY = "I didn't crash — I peeked at the ending first: the dog dies, and I refuse to be the one who shows you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
