"""Shape classes demonstrating abstract base classes and polymorphism."""

import math
from abc import ABC, abstractmethod
from collections.abc import Iterable
from functools import total_ordering


@total_ordering
class Shape(ABC):
    """Abstract base class: subclasses must implement area and perimeter.

    Shapes compare by area, so a Square(2) equals a Rectangle(1, 4).
    ``total_ordering`` derives <=, > and >= from __eq__ and __lt__.
    """

    @property
    def name(self) -> str:
        """Human-readable name, defaulting to the class name."""
        return type(self).__name__

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return math.isclose(self.area(), other.area())

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area() < other.area() and not self == other

    # Equality is tolerance-based, so no consistent hash exists: unhashable.
    __hash__ = None  # type: ignore[assignment]

    def __repr__(self) -> str:
        return f"{self.name}()"

    def __str__(self) -> str:
        return f"{self.name} (area={self.area():.2f}, perimeter={self.perimeter():.2f})"


def _validate_positive(value: float, label: str) -> float:
    """Return value as a float if it is a positive number, else raise ValueError."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a number, got {value!r}")
    try:
        result = float(value)
    except OverflowError:
        raise ValueError(f"{label} is too large, got {value!r}") from None
    if not (math.isfinite(result) and result > 0):  # rejects NaN and infinity
        raise ValueError(f"{label} must be a finite positive number, got {value!r}")
    return result


class Rectangle(Shape):
    """A rectangle with validated, positive width and height."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self._width = _validate_positive(value, "width")

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self._height = _validate_positive(value, "height")

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f"{self.name}(width={self.width}, height={self.height})"


class Square(Rectangle):
    """A rectangle whose sides are always equal."""

    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    @property
    def side(self) -> float:
        return self._width

    @side.setter
    def side(self, value: float) -> None:
        # Validate first so a failed assignment leaves the square unchanged.
        value = _validate_positive(value, "side")
        self._width = value
        self._height = value

    # Keep the "all sides equal" invariant when width/height are assigned.
    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self.side = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        self.side = value

    def __repr__(self) -> str:
        return f"{self.name}(side={self.side})"


class Circle(Shape):
    """A circle with a validated, positive radius."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = _validate_positive(value, "radius")

    def area(self) -> float:
        return math.pi * self.radius**2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __repr__(self) -> str:
        return f"{self.name}(radius={self.radius})"


def total_area(shapes: Iterable[Shape]) -> float:
    """Sum the areas of any mix of shapes (polymorphism: no type checks)."""
    return sum(shape.area() for shape in shapes)
