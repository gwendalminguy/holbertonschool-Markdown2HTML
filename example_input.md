# Markdown2HTML Test File

## Some Testing

### Paragraphs

This text should be parsed as a simple paragraph in the output.

And this text should appear as a second
paragraph on two separated lines.

### Lists

* first item
* second item
* third item

Two separated lists are correctly parsed as two distinct lists.

- TEST A
- TEST B
- TEST C

- TEST A
- TEST B
- TEST C

## More Testing

### Bold & Emphasis

This is how **bold text** is parsed.
This is how __emphasized text__ is parsed.

**A whole line works as well.**

Even on two different lines, **bold
text** should be correctly parsed.

### C Removal & MD5 Hashing

- C Removal: ((This text won't contain «C» anymore...))
- MD5 Hashing: [[This text will be hashed with MD5...]]
