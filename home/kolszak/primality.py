"""
Check if given number is prime.
"""

import unittest
import math


def is_prime(n: int) -> bool:
    """Check id given number is prime."""
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


class IsPrimeTest(unittest.TestCase):
    """is_prime function tests."""

    def test_is_prime_test(self):
        """Test some small hand picked example."""
        self.assertEqual(is_prime(78), False)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(21), False)

