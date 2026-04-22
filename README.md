# Markdown2HTML

This project consists of a Python script that converts Markdown syntax into HTML.

## Description

The script requires two command-line arguments: an input file (which must be a Markdown file), and the name of the output file. It supports the following elements:

- Headings (`# <title>`)
- Unordered Lists (`- <element>`)
- Ordered Lists (`* <element>`)
- Paragraphs
- Bold Texts (`**<text>**`)
- Emphasized Texts (`__<text>__`)

It can also perform two custom transformations using specific delimiters:

- "C" Removal (`((<text>))`) - Removes all occurences of the letter "C" (case-insensitive) from the text
- MD5 Hashing (`[[<text>]]`) - Hashes the text using the [MD5 algorithm](https://en.wikipedia.org/wiki/MD5)

## Installation

Installation can be done simply by downloading the `markdown2html.py` file, or by cloning this repository using the following commands:

```bash
git clone git@github.com:gwendalminguy/holbertonschool-Markdown2HTML.git
cd holbertonschool-Markdown2HTML
chmod u+x markdown2html.py
```

## Usage

The script can be launched using the following command:

```bash
./markdown2html.py <input_file.md> <output_file.html>
```

## Error Handling

The script exits with an error if:

- the number of arguments is incorrect
- the input file does not exist
