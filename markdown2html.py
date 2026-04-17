#!/usr/bin/python3
"""
markdown2html.py
Script generating HTML from Markdown syntax.
"""

import os
import sys


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    input_file_name = sys.argv[1]
    input_file_path = os.path.abspath(input_file_name)

    output_file_name = sys.argv[2]
    output_file_path = os.path.abspath(output_file_name)

    # Check for input file existence
    if not os.path.exists(input_file_path):
        sys.stderr.write(f"Missing {input_file_name}\n")
        sys.exit(1)

    # Read input file lines as a list
    with open(input_file_path, "r", encoding="utf-8") as file:
        elements = file.readlines()

    headings = {
        "#": "h1",
        "##": "h2",
        "###": "h3",
        "####": "h4",
        "#####": "h5",
        "######": "h6",
    }

    parsed = []
    ul_active = False

    for line in elements:
        line = line.strip()

        # Ignore empty lines
        if len(line) == 1:
            continue

        content = line.split(" ")

        # Ignore tag only
        if len(content) == 1:
            continue

        tag = content[0]
        text = " ".join(content[1:])

        # Close unordered list if necessary
        if ul_active and tag != "-":
            parsed.append("</ul>\n")

        # Heading tag
        if tag in headings.keys():
            parsed.append(f"<{headings[tag]}>{text}</{headings[tag]}>\n")
            continue

        # List tag
        if tag == "-":
            # Start unordered list
            if not ul_active:
                parsed.append("<ul>\n")
                ul_active = True

            parsed.append(f"<li>{text}</li>\n")

    # Write output file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write("".join(parsed))

    sys.exit(0)


if __name__ == "__main__":
    main()
