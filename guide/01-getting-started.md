# Chapter 1: Getting Started with Python

Welcome! This chapter takes you from nothing to running your first Python program, and introduces the core building blocks you'll use everywhere: values, variables, and basic types.

## 1.1 Installing Python

Python 3.10 or newer is recommended. Check what you have:

```bash
python3 --version
```

If it's missing or old, install it from [python.org](https://www.python.org/downloads/) or with your package manager (`brew install python`, `apt install python3`, `winget install Python.Python.3`).

## 1.2 Hello, World

Create a file named `hello.py`:

```python
print("Hello, World!")
```

Run it:

```bash
python3 hello.py
```

You should see `Hello, World!`. `print` is a built-in *function*; the text in quotes is a *string*.

## 1.3 The interactive interpreter (REPL)

Run `python3` with no arguments to get a prompt where each line is evaluated immediately:

```pycon
>>> 2 + 3
5
>>> "py" * 3
'pypypy'
>>> exit()
```

The REPL is ideal for quick experiments.

## 1.4 Variables

A variable is a name bound to a value. No type declaration is needed:

```python
name = "Ada"
age = 36
height = 1.68
is_student = False
```

Names are case-sensitive, may contain letters, digits and underscores, and can't start with a digit. By convention Python uses `snake_case`.

## 1.5 Basic types

| Type    | Example          | Notes                         |
|---------|------------------|-------------------------------|
| `int`   | `42`             | Arbitrary precision           |
| `float` | `3.14`           | 64-bit binary floating point  |
| `str`   | `"hello"`        | Immutable text                |
| `bool`  | `True`, `False`  | Subclass of `int`             |
| `None`  | `None`           | "No value"                    |

Inspect a type with `type()`:

```python
print(type(42))      # <class 'int'>
print(type("hi"))    # <class 'str'>
```

## 1.6 Arithmetic

```python
print(7 + 2)    # 9
print(7 - 2)    # 5
print(7 * 2)    # 14
print(7 / 2)    # 3.5   (true division, always a float)
print(7 // 2)   # 3     (floor division)
print(7 % 2)    # 1     (remainder)
print(7 ** 2)   # 49    (power)
```

## 1.7 Working with strings

```python
first = "Ada"
last = "Lovelace"

full = first + " " + last
print(full)                      # Ada Lovelace
print(len(full))                 # 12
print(full.upper())              # ADA LOVELACE
print(f"Hello, {first}! 2+2={2 + 2}")   # f-string
```

f-strings (prefix `f`) embed expressions inside `{}` and are the preferred way to format text.

## 1.8 Input and output

```python
name = input("What is your name? ")
print(f"Nice to meet you, {name}!")
```

`input()` always returns a string. Convert when you need a number:

```python
age = int(input("Age? "))
print(f"Next year you'll be {age + 1}.")
```

## 1.9 Comments

```python
# This is a comment
x = 10  # so is this
```

## 1.10 Common mistakes

- **Mixing types:** `"age: " + 5` raises `TypeError`. Use `f"age: {5}"` or `str(5)`.
- **Indentation:** Python uses indentation for structure; inconsistent spacing raises `IndentationError`.
- **Misspelled names:** using an undefined variable raises `NameError`.

## Exercises

1. Write a program that asks for your name and prints a greeting.
2. Compute the area of a circle with radius `5` (use `3.14159`).
3. Ask for two numbers and print their sum, difference, and quotient.
4. What does `type(7 / 2)` return? What about `type(7 // 2)`? Verify in the REPL.

## Summary

You installed Python, ran a script, used the REPL, and learned about variables, basic types, arithmetic, strings, and input/output. Next chapter: control flow with `if`, `for`, and `while`.
