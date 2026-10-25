#!/usr/bin/env python3
"""Small command line entry point for the Yemeni judicial formatter."""

import argparse

from yemeni_judicial_formatter import format_judicial_text


def main() -> None:
    parser = argparse.ArgumentParser(description="Format Yemeni judicial text.")
    parser.add_argument("text", help="Arabic or mixed-language judicial text to normalize.")
    args = parser.parse_args()
    print(format_judicial_text(args.text))


if __name__ == "__main__":
    main()
