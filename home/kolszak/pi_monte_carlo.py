"""
Calculate the PI value using monte carlo method.
"""
import unittest
import random
import math


def pi(n: int) -> float:
    values_in = 0
    values_count = 0
    for _ in range(n):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        if x ** 2 + y ** 2 <= 1:
            values_in += 1
        values_count += 1
    if values_count == 0:
        return math.inf
    return 4 * values_in / values_count


print(pi(1000000))


class PiMonteCarloTest(unittest.TestCase):
    """Unit tests for area functions"""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples"""
        self.assertTrue(abs(pi(1000000) - 3.14) < 0.01)

