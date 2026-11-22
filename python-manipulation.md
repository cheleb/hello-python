# Chapter: Python Manipulation

This chapter covers how to manipulate the core data types in Python: strings, lists, tuples, dictionaries, sets, and files. Every snippet can be run as-is with Python 3.9+.

## 1. Strings

Strings are immutable sequences of characters. Every "modification" returns a new string.

```python
s = "  Hello, Python!  "

print(s.strip())             # 'Hello, Python!'
print(s.lower())             # '  hello, python!  '
print(s.replace("Python", "World"))
print(s.strip().split(", "))  # ['Hello', 'Python!']
print("-".join(["a", "b", "c"]))  # 'a-b-c'
```

### Slicing

```python
word = "manipulation"
print(word[0])      # 'm'
print(word[-1])     # 'n'
print(word[0:5])    # 'manip'
print(word[::-1])   # 'noitalupinam' (reversed)
```

### Formatting

```python
name, score = "Ada", 97.456
print(f"{name} scored {score:.1f}")   # Ada scored 97.5
print(f"{name:>10}|{score:08.2f}")    # right-align, zero-pad
```

## 2. Lists

Lists are ordered, mutable sequences.

```python
nums = [3, 1, 4, 1, 5]

nums.append(9)          # add at end
nums.insert(0, 2)       # add at index
nums.remove(1)          # remove first matching value
last = nums.pop()       # remove and return last item
nums.sort()             # in place
print(sorted(nums, reverse=True))  # new list
```

### Comprehensions

```python
squares = [n * n for n in range(10)]
evens = [n for n in squares if n % 2 == 0]
pairs = [(x, y) for x in "ab" for y in (1, 2)]
```

### Useful built-ins

```python
data = [4, 8, 15, 16, 23, 42]
print(len(data), sum(data), min(data), max(data))
for i, value in enumerate(data, start=1):
    print(i, value)
for a, b in zip(data, data[1:]):
    print(b - a)
```

> **Pitfall:** `b = a` does not copy a list; both names refer to the same object. Use `a.copy()`, `a[:]` or `list(a)` for a shallow copy, and `copy.deepcopy(a)` for nested data.

## 3. Tuples

Tuples are immutable, which makes them hashable (when their items are) and safe as dictionary keys.

```python
point = (3, 4)
x, y = point                 # unpacking
first, *rest = (1, 2, 3, 4)  # first=1, rest=[2, 3, 4]
a, b = 1, 2
a, b = b, a                  # swap
```

## 4. Dictionaries

Dictionaries map keys to values and preserve insertion order.

```python
user = {"name": "Ada", "age": 36}

user["email"] = "ada@example.com"      # add / update
print(user.get("phone", "n/a"))         # safe lookup with default
user.pop("age")                         # remove
user.update({"age": 37, "city": "London"})

for key, value in user.items():
    print(key, "=>", value)

merged = {"a": 1} | {"b": 2}            # Python 3.9+
inverted = {v: k for k, v in {"a": 1, "b": 2}.items()}
```

### Counting and grouping

```python
from collections import Counter, defaultdict

print(Counter("mississippi").most_common(2))   # [('i', 4), ('s', 4)]

groups = defaultdict(list)
for word in ["apple", "avocado", "banana", "blueberry"]:
    groups[word[0]].append(word)
print(dict(groups))
```

## 5. Sets

Sets hold unique, unordered items and support fast membership tests.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

print(a | b)   # union        {1, 2, 3, 4, 5}
print(a & b)   # intersection {3, 4}
print(a - b)   # difference   {1, 2}
print(a ^ b)   # symmetric    {1, 2, 5}

unique = list(dict.fromkeys([3, 1, 3, 2, 1]))  # dedupe, keep order
```

## 6. Files

Use `pathlib` and context managers so files are always closed.

```python
from pathlib import Path

path = Path("notes.txt")
path.write_text("first line\nsecond line\n", encoding="utf-8")

print(path.read_text(encoding="utf-8"))

with path.open("a", encoding="utf-8") as f:
    f.write("third line\n")

with path.open(encoding="utf-8") as f:
    for line in f:                 # lazy, memory-friendly
        print(line.rstrip())
```

### JSON

```python
import json

payload = {"name": "Ada", "langs": ["python", "c"]}
text = json.dumps(payload, indent=2)
assert json.loads(text) == payload
```

## 7. Putting it together: word frequency

```python
from collections import Counter
from pathlib import Path
import re


def top_words(path: str, n: int = 5) -> list[tuple[str, int]]:
    text = Path(path).read_text(encoding="utf-8").lower()
    words = re.findall(r"[a-z']+", text)
    return Counter(words).most_common(n)


if __name__ == "__main__":
    Path("notes.txt").write_text("the cat and the hat\n", encoding="utf-8")
    print(top_words("notes.txt"))   # [('the', 2), ('cat', 1), ('and', 1), ('hat', 1)]
```

## Exercises

1. Write a function that returns whether a string is a palindrome, ignoring case and punctuation.
2. Given a list of numbers, return a list of the running totals.
3. Group a list of words by length into a dictionary.
4. Read two text files and print the words they have in common.
5. Merge two dictionaries, summing the values of shared keys.

## Summary

| Type       | Ordered | Mutable | Duplicates | Typical use            |
|------------|---------|---------|------------|------------------------|
| `str`      | yes     | no      | yes        | text                   |
| `list`     | yes     | yes     | yes        | sequences of items     |
| `tuple`    | yes     | no      | yes        | fixed records, keys    |
| `dict`     | yes     | yes     | unique keys| lookups, grouping      |
| `set`      | no      | yes     | no         | membership, dedupe     |
