# RegEx

## 1. Declarative languages

In imperative languages:
- A "program" is a description of computational processes
- The interpreter carries out execution/evaluation rules

In declarative languages:
- A "program" is a description of the desired result
- The interpreter figures out how to generate the result

## 2. Regular expression syntax

### Matching Exact Strings

The following are special characters in regular expressions: `\ ( ) [ ] { } + * ? | $ ^ .`

if the matched string contains special characters, they must be escaped using a backslash.

### character class

<img src=".\assets\week6\cc.png" alt="character class" style="zoom:30%;" />

### quantifiers

<img src=".\assets\week6\q.png" alt="quantifiers" style="zoom:30%;" />

### Combining Patterns

Patterns `P₁` and `P₂` can be combined in various ways.

<img src=".\assets\week6\cp.png" alt="Combining Patterns" style="zoom:30%;" />

### Anchors

These don't match an actual character, they indicate the position where the surrounding pattern should be found.

<img src=".\assets\week6\a.png" alt="Anchors" style="zoom:30%;" />

## 3. Regular expressions in Python

### Raw strings

In normal Python strings, a backslash indicates an escape sequence, like \n for new line.
But backslash has a special meaning in regular expressions. To make it easy to write regular expressions in Python strings, use raw strings by prefixing the string with an ***`r`***:
``` python
pattern = r"\b[ab]+\b"
```

### The re module

The re module provides many helpful functions.


<img src=".\assets\week6\re.png" alt="re" style="zoom:30%;" />

### Match Objects

The functions re.search, re.match, and re.fullmatch all take a string containing a regular expression and a string of text. They return either a `Match` object or, if there is no match, `None`.

***Match objects are treated as true values, so you can use the result as a boolean:***
``` python
bool(re.search(r'-?\d+', '123'))           # True
bool(re.search(r'-?\d+', 'So many peeps')) # False
```

### Inspecting a match

Match objects carry information about what has been matched.

The `Match.group()` method allows you to retrieve it.

``` python
x = "This string contains 35 characters."
mat = re.search(r'\d+', x)
mat.group(0)  # 35
```

### Match Groups

If there are parentheses in a patterns, each of the parenthesized groups will become groups in the match object.

``` python
x = "There were 12 pence in a shilling and 20 shillings in a pound."
mat = re.search(r'(\d+)[a-z\s]+(\d+)', x)

mat.group(0)  # '12 pence in a shilling and 20'
mat.group(1)  # 12
mat.group(2)  # 20
mat.groups()  # (12, 20)
```
