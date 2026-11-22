"""Shape classes demonstrating abstract base classes and polymorphism."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class: subclasses must implement area and perimeter."""

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

    def __repr__(self) -> str:
        return f"{self.name}()"

    def __str__(self) -> str:
        return f"{self.name} (area={self.area():.2f}, perimeter={self.perimeter():.2f})"
