#!/usr/bin/python3
"""
markdown2html.py
Script generating HTML from Markdown syntax.
"""

import os
import re
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
    ol_active = False
    p_active = False

    for line in elements:
        line = line.strip()

        # Ignore empty lines
        if len(line) < 1:
            # Close paragraph if necessary
            if p_active:
                parsed.append("</p>\n")
                p_active = False
            continue

        content = line.split(" ")

        tag = content[0] if content[0] in headings.keys() or content[0] in ["-", "*"] else None

        # Ignore tag only
        if tag and len(content) == 1:
            # Close paragraph if necessary
            if p_active:
                parsed.append("</p>\n")
                p_active = False
            continue

        text = " ".join(content[1:]) if tag else " ".join(content)

        # Close unordered list if necessary
        if ul_active and tag != "-":
            parsed.append("</ul>\n")
            ul_active = False

        # Close ordered list if necessary
        if ol_active and tag != "*":
            parsed.append("</ol>\n")
            ol_active = False

        # Close paragraph if necessary
        if p_active and tag:
            parsed.append("</p>\n")
            p_active = False

        # Heading tag
        if tag in headings.keys():
            parsed.append(f"<{headings[tag]}>{text}</{headings[tag]}>\n")
            continue

        # Unordered list tag
        elif tag == "-":
            # Start unordered list
            if not ul_active:
                parsed.append("<ul>\n")
                ul_active = True

            parsed.append(f"<li>{text}</li>\n")

        # Ordered list tag
        elif tag == "*":
            # Start ordered list
            if not ol_active:
                parsed.append("<ol>\n")
                ol_active = True

            parsed.append(f"<li>{text}</li>\n")

        # Paragraph
        elif not tag:
            if not p_active:
                parsed.append("<p>\n")
                p_active = True
            else:
                parsed.append("<br>\n")
            parsed.append(f"{text}\n")

    # Close unordered list if necessary
    if ul_active:
        parsed.append("</ul>\n")

    # Close ordered list if necessary
    if ol_active:
        parsed.append("</ol>\n")

    # Close paragraph if necessary
    if p_active:
        parsed.append("</p>\n")

    result = "".join(parsed)

    # Bold text (**)
    bold = re.findall(r"\*\*[\s\S]*?\*\*", result)
    for element in bold:
        result = result.replace(element, f"<b>{element[2:-2]}</b>")

    # Emphasis text (__)
    emphasis = re.findall(r"\_\_[\s\S]*?\_\_", result)
    for element in emphasis:
        result = result.replace(element, f"<em>{element[2:-2]}</em>")

    # Write output file
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(result)

    sys.exit(0)


if __name__ == "__main__":
    main()
