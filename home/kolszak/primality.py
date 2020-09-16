"""
Check if given number is prime.
Check if given number is perfect.
Get divisors of given number.
"""

import unittest
import math
from typing import Set


def is_prime(n: int) -> bool:
    """Check if given number is prime."""
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def get_divisors(n: int) -> Set[int]:
    """Get divisors of given number."""

    def _get_divisors_in(n: int, last_mod: int) -> Set[int]:
        if n == 1:
            return {1}
        while n % last_mod != 0:
            last_mod += 1
        inner = _get_divisors_in(n // last_mod, last_mod)
        multiplied = {last_mod * a for a in inner}
        return multiplied | inner

    result = _get_divisors_in(n, 2)
    result.remove(n)
    return result


def is_perfect(n: int) -> bool:
    """Check if given number is perfect."""
    divs = get_divisors(n)
    s = 0
    for d in divs:
        s += d
    return s == n


class PrimalityTest(unittest.TestCase):
    """is_prime function tests."""

    def test_is_prime(self):
        """Test some small hand picked example."""
        self.assertEqual(is_prime(78), False)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(21), False)

    def test_is_perfect(self):
        """Test some small hand picked example."""
        self.assertEqual(is_perfect(6), True)
        self.assertEqual(is_perfect(496), True)
        self.assertEqual(is_perfect(189), False)

