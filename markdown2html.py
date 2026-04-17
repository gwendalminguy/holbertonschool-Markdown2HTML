#!/usr/bin/python3
"""
markdown2html.py
Script generating HTML from Markdown syntax.
"""

import os
import sys

if len(sys.argv) != 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

input_file_name = sys.argv[1]
input_file_path = os.path.abspath(input_file_name)

output_file_name = sys.argv[2]
output_file_path = os.path.abspath(output_file_name)

if not os.path.exists(input_file_path):
    sys.stderr.write(f"Missing {input_file_name}\n")
    sys.exit(1)

sys.exit(0)
