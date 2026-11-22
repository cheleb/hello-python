import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fizzbuzz import fizzbuzz, fizzbuzz_range


class FizzBuzzTest(unittest.TestCase):
    def test_plain_number(self):
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")

    def test_multiple_of_three(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_multiple_of_five(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_multiple_of_both(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_range(self):
        self.assertEqual(
            fizzbuzz_range(5), ["1", "2", "Fizz", "4", "Buzz"]
        )


if __name__ == "__main__":
    unittest.main()
