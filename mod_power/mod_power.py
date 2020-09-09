"""
This module computes a ** p mod n without using numbers that are significantly larger than n.
"""

import unittest


def mod_power(a: int, p: int, n: int) -> int:
    """Compute a ** p mod n"""

    return (a ** p) % n


class ModPowerTest(unittest.TestCase):
    """Unit tests for mod_power functions"""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples"""
        self.assertEqual(mod_power(2, 5, 100), 32)
        self.assertEqual(mod_power(2, 5, 10), 2)
        self.assertEqual(mod_power(5, 2, 10), 5)


if __name__ == '__main__':
    print(mod_power(9, 9**2, 1000000))
