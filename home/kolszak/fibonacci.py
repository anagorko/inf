"""
Compute fibonacci numbers.
"""

import unittest


def fibonacci_recursive(n: int) -> int:
    """Compute fibonacci number with given index using recursion."""
    if 1 <= n <= 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n: int) -> int:
    """Compute fibonacci number with given index using iteration."""
    a, b = 1, 1
    if 1 <= n <= 2:
        return a
    for i in range(n - 2):
        c = b
        b = a + b
        a = c
    return b


class FibonacciTest(unittest.TestCase):
    """Fibonacci compute functions tests."""

    def test_fibonacci_iterative(self):
        """Test some small hand picked example."""
        self.assertEqual(fibonacci_iterative(6), 8)
        self.assertEqual(fibonacci_iterative(7), 13)
        self.assertEqual(fibonacci_iterative(8), 21)

    def test_fibonacci_recursive(self):
        """Test some small hand picked example."""
        self.assertEqual(fibonacci_recursive(6), 8)
        self.assertEqual(fibonacci_recursive(7), 13)
        self.assertEqual(fibonacci_recursive(8), 21)

