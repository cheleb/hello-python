import contextlib
import io
import unittest

from oop.main import main


class MainTest(unittest.TestCase):
    def run_main(self) -> str:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            main()
        return buffer.getvalue()

    def test_prints_each_section(self) -> None:
        output = self.run_main()
        self.assertIn("Shapes:", output)
        self.assertIn("Sorted by area:", output)
        self.assertIn("Rectangle (area=12.00, perimeter=14.00)", output)

    def test_sorted_section_is_ascending(self) -> None:
        sorted_part = self.run_main().split("Sorted by area:")[1]
        areas = [
            float(line.split("area=")[1].split(",")[0])
            for line in sorted_part.splitlines()
            if "area=" in line
        ]
        self.assertEqual(areas, sorted(areas))
        self.assertEqual(len(areas), 4)

    def test_reports_largest_and_equality(self) -> None:
        output = self.run_main()
        self.assertIn("Largest: Rectangle(width=3.0, height=4.0)", output)
        self.assertIn("Square(2) == Rectangle(1, 4): True", output)

    def test_total_area(self) -> None:
        self.assertIn("Total area: 27.07", self.run_main())


if __name__ == "__main__":
    unittest.main()
