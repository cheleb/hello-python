"""FizzBuzz, built test-first (see tests/test_fizzbuzz.py)."""


def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def fizzbuzz_range(last: int) -> list[str]:
    return [fizzbuzz(i) for i in range(1, last + 1)]
