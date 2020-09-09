"""
Finding all divisors of a number.
"""

from typing import List, Set
import unittest


def divisors(number: int) -> List[int]:
    """Compute a sorted list of all positive divisors of a given number."""
    result = list()
    for divisor in range(1, number+1):
        if number % divisor == 0:
            result.append(divisor)
    return result


def divisors2(number: int) -> List[int]:
    """Compute an unsorted list of all positive divisors of a given number."""
    result = list()
    divisor = 1
    while divisor * divisor <= number:
        if number % divisor == 0:
            result.append(divisor)
            if divisor != number // divisor:
                result.append(number // divisor)
        divisor = divisor + 1

    return result


def divisors3(number: int) -> Set[int]:
    """Compute a set of all positive divisors of a given mumber"""

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            smaller_result = divisors3(number // divisor)
            multiplied_result = {d * divisor for d in smaller_result}

            return smaller_result | multiplied_result
        divisor = divisor + 1

    return {1, number}


class DivisorTest(unittest.TestCase):
    """Unit tests for divisor functions."""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples."""
        self.assertListEqual(divisors(12), [1, 2, 3, 4, 6, 12])

    def test_divisors2(self):
        """Test divisors2 vs divisors."""
        for test_case in range(1, 1000):
            result = divisors(test_case)
            result2 = sorted(divisors2(test_case))

            self.assertListEqual(result, result2)

    def test_divisors3(self):
        """Test divisors3 vs divisors."""
        for test_case in range(1, 1000):
            result = divisors(test_case)
            result2 = sorted(divisors3(test_case))

            self.assertListEqual(result, result2)


if __name__ == '__main__':
    print(sorted(divisors3(10 ** 400)))
