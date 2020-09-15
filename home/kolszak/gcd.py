"""
Compute greatest common divisor.
"""

import unittest


def gcd_recursive(a: int, b: int) -> int:
    """Compute gcd using recursion."""
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)


def gcd_iterative(a: int, b: int) -> int:
    """Compute gcd using iteration."""
    while a % b != 0:
        c = b
        b = a % b
        a = c
    return b


class GcdTest(unittest.TestCase):
    """Gcd compute functions tests."""

    def gcd_recursive_test(self):
        """Test some small hand picked example."""
        self.assertEqual(gcd_recursive(48, 18), 6)
        self.assertEqual(gcd_recursive(123, 369), 123)
        self.assertEqual(gcd_recursive(8, 12), 4)
        self.assertEqual(gcd_recursive(12, 8), 4)

    def gcd_iterative_test(self):
        """Test some small hand picked example."""
        self.assertEqual(gcd_iterative(48, 18), 6)
        self.assertEqual(gcd_iterative(123, 369), 123)
        self.assertEqual(gcd_iterative(8, 12), 4)
        self.assertEqual(gcd_iterative(12, 8), 4)

