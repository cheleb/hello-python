"""Demo: build a mix of shapes, print them, sort them, and total their areas."""

from oop.shapes import Circle, Rectangle, Shape, Square, total_area


def build_shapes() -> list[Shape]:
    return [Rectangle(3, 4), Circle(1.5), Square(2), Rectangle(1, 4)]


def main() -> None:
    shapes = build_shapes()

    print("Shapes:")
    for shape in shapes:
        print(f"  {shape}")

    print("\nSorted by area:")
    for shape in sorted(shapes):
        print(f"  {shape}")

    print(f"\nLargest: {max(shapes)!r}")
    print(f"Square(2) == Rectangle(1, 4): {Square(2) == Rectangle(1, 4)}")
    print(f"Total area: {total_area(shapes):.2f}")


if __name__ == "__main__":
    main()
