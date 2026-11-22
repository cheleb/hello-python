# OOP in Python: a shapes example

A small, stdlib-only (Python 3.10+) example showing core object-oriented
concepts with geometric shapes.

## Layout

| Path | Purpose |
| --- | --- |
| `oop/shapes.py` | `Shape`, `Rectangle`, `Square`, `Circle`, `total_area` |
| `oop/main.py` | Runnable demo |
| `tests/` | `unittest` tests for shapes and the demo |

## Concepts and where to find them

- **Abstraction** — `Shape` in `oop/shapes.py` is an abstract base class
  (`ABC`) with abstract methods `area` and `perimeter`. It cannot be
  instantiated; every concrete shape must implement both.
- **Inheritance** — `Rectangle` and `Circle` extend `Shape`; `Square` extends
  `Rectangle` and reuses its logic via `super().__init__`.
- **Encapsulation** — `width`, `height`, `radius` and `side` are properties
  backed by private-by-convention attributes (`_width`, ...). Setters validate
  through `_validate_positive` and raise `ValueError` for invalid input, so a
  shape can never hold a bad value. `Square` overrides the setters to keep its
  sides equal.
- **Polymorphism** — `total_area` and `main.py` treat any mix of shapes
  uniformly by calling `area()`, with no type checks.
- **Special methods** — `Shape` defines `__eq__` and `__lt__` (compare by
  area; `functools.total_ordering` derives the rest), plus `__repr__` and
  `__str__`. This is why `sorted(shapes)` and `max(shapes)` work, and why
  `Square(2) == Rectangle(1, 4)`.

## Run the demo

```sh
python -m oop.main
```

## Run the tests

From the repository root:

```sh
python -m unittest discover -s tests
```
