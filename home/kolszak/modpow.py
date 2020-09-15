"""
Recursive (a ** b) % m.
"""

import unittest


def power(a: int, p: int, m: int) -> int:
    """Compute (a ** p) % m."""
    if p == 0:
        return 1
    if p % 2 == 1:
        return (a * pow(a * a, p // 2, m)) % m
    if p % 2 == 0:
        return pow(a * a, p // 2, m) % m


class ModPowerUnitTest(unittest.TestCase):
    """Unit tests for power function."""

    def test_mod_power(self):
        """Test some small hand picked example."""
        for i in range(10):
            for j in range(10):
                for m in range(10):
                    self.assertEqual(power(i, j, m), (i ** j) % m)

