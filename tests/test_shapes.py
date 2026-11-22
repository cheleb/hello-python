import unittest

from oop.shapes import Shape


class UnitSquare(Shape):
    def area(self) -> float:
        return 1.0

    def perimeter(self) -> float:
        return 4.0


class ShapeTest(unittest.TestCase):
    def test_cannot_instantiate_abstract_shape(self) -> None:
        with self.assertRaises(TypeError):
            Shape()  # type: ignore[abstract]

    def test_incomplete_subclass_cannot_be_instantiated(self) -> None:
        class NoPerimeter(Shape):
            def area(self) -> float:
                return 0.0

        with self.assertRaises(TypeError):
            NoPerimeter()  # type: ignore[abstract]

    def test_trivial_subclass_works(self) -> None:
        square = UnitSquare()
        self.assertEqual(square.area(), 1.0)
        self.assertEqual(square.perimeter(), 4.0)

    def test_name_defaults_to_class_name(self) -> None:
        self.assertEqual(UnitSquare().name, "UnitSquare")

    def test_repr_and_str(self) -> None:
        square = UnitSquare()
        self.assertEqual(repr(square), "UnitSquare()")
        self.assertEqual(str(square), "UnitSquare (area=1.00, perimeter=4.00)")


if __name__ == "__main__":
    unittest.main()
