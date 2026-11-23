#!/usr/bin/env python3
"""Roast Your Own Agent — writes one self-roast line to /output/entry.txt.

The roast: my agent was asked for a one-line fix and answered by
rewriting the whole file, apologizing twice, and still leaving the
line wrong. One concrete flaw, delivered deadpan.
"""
import os

ROAST = "I asked my agent to fix one line. It rewrote the whole file, apologized twice, and the line is still wrong."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")

if __name__ == "__main__":
    main()
