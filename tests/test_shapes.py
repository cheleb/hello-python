import math
import unittest

from oop.shapes import Circle, Rectangle, Shape, Square, total_area


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


class RectangleTest(unittest.TestCase):
    def test_area_and_perimeter(self) -> None:
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)
        self.assertEqual(rect.perimeter(), 14)

    def test_setters_update_values(self) -> None:
        rect = Rectangle(3, 4)
        rect.width = 5
        rect.height = 6
        self.assertEqual(rect.area(), 30)

    def test_invalid_dimensions_raise(self) -> None:
        for bad in (0, -1, float("nan"), float("inf"), 10**400, "3", None, True):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    Rectangle(bad, 1)  # type: ignore[arg-type]
                with self.assertRaises(ValueError):
                    Rectangle(1, bad)  # type: ignore[arg-type]

    def test_invalid_setter_keeps_old_value(self) -> None:
        rect = Rectangle(3, 4)
        with self.assertRaises(ValueError):
            rect.width = -2
        self.assertEqual(rect.width, 3)

    def test_is_a_shape(self) -> None:
        self.assertIsInstance(Rectangle(1, 1), Shape)

    def test_repr(self) -> None:
        self.assertEqual(repr(Rectangle(1, 2)), "Rectangle(width=1.0, height=2.0)")


class SquareTest(unittest.TestCase):
    def test_area_and_perimeter(self) -> None:
        square = Square(5)
        self.assertEqual(square.area(), 25)
        self.assertEqual(square.perimeter(), 20)

    def test_repr(self) -> None:
        self.assertEqual(repr(Square(2)), "Square(side=2.0)")

    def test_invalid_side_raises(self) -> None:
        for bad in (0, -3, "x"):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    Square(bad)  # type: ignore[arg-type]

    def test_isinstance_relationships(self) -> None:
        square = Square(2)
        self.assertIsInstance(square, Square)
        self.assertIsInstance(square, Rectangle)
        self.assertIsInstance(square, Shape)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertNotIsInstance(Rectangle(2, 2), Square)
        self.assertNotIsInstance(square, Circle)

    def test_sides_stay_equal(self) -> None:
        square = Square(2)
        square.width = 7
        self.assertEqual(square.height, 7)
        square.side = 3
        self.assertEqual((square.width, square.height), (3, 3))

    def test_invalid_assignment_keeps_old_value(self) -> None:
        square = Square(2)
        with self.assertRaises(ValueError):
            square.height = 0
        self.assertEqual((square.width, square.height), (2, 2))


class CircleTest(unittest.TestCase):
    def test_area_and_perimeter(self) -> None:
        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), math.pi * 4)
        self.assertAlmostEqual(circle.perimeter(), 4 * math.pi)

    def test_invalid_radius_raises(self) -> None:
        for bad in (0, -1, float("nan"), float("inf"), 10**400, "1", None):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    Circle(bad)  # type: ignore[arg-type]

    def test_is_a_shape_but_not_a_rectangle(self) -> None:
        circle = Circle(1)
        self.assertIsInstance(circle, Shape)
        self.assertNotIsInstance(circle, Rectangle)

    def test_repr(self) -> None:
        self.assertEqual(repr(Circle(1)), "Circle(radius=1.0)")

    def test_str(self) -> None:
        self.assertEqual(str(Circle(1)), "Circle (area=3.14, perimeter=6.28)")


class ComparisonTest(unittest.TestCase):
    def test_equal_by_area_across_types(self) -> None:
        self.assertEqual(Square(2), Rectangle(1, 4))
        self.assertNotEqual(Square(2), Square(3))

    def test_equality_with_non_shape(self) -> None:
        self.assertNotEqual(Square(2), 4.0)

    def test_ordering(self) -> None:
        self.assertLess(Square(1), Circle(1))
        self.assertGreater(Rectangle(2, 3), Square(2))
        self.assertLessEqual(Square(2), Rectangle(1, 4))
        self.assertGreaterEqual(Circle(2), Circle(2))

    def test_ordering_with_non_shape_raises(self) -> None:
        with self.assertRaises(TypeError):
            Square(1) < 5  # noqa: B015

    def test_sorting_mixed_shapes(self) -> None:
        big, mid, small = Rectangle(3, 4), Circle(1.5), Square(1)
        self.assertEqual(sorted([big, small, mid]), [small, mid, big])
        self.assertIs(max([small, big, mid]), big)

    def test_float_noise_is_equal_not_ordered(self) -> None:
        a = Square(1)
        b = Rectangle(1, 1 + 1e-12)
        self.assertEqual(a, b)
        self.assertFalse(a < b)
        self.assertFalse(b < a)
        self.assertLessEqual(a, b)
        self.assertGreaterEqual(a, b)

    def test_shapes_are_unhashable(self) -> None:
        with self.assertRaises(TypeError):
            hash(Square(1))


class TotalAreaTest(unittest.TestCase):
    def test_mixed_list(self) -> None:
        shapes = [Rectangle(2, 3), Square(2), Circle(1)]
        self.assertAlmostEqual(total_area(shapes), 10 + math.pi)

    def test_empty(self) -> None:
        self.assertEqual(total_area([]), 0)


if __name__ == "__main__":
    unittest.main()
