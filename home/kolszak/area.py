"""
Calculate the area under the graph.
"""
from typing import Callable
import unittest


def area(func: Callable[[float], float], interval_start: float, interval_end: float, precision: float) -> float:
    """Calculates the integral of a function in a given interval."""
    a = interval_start
    result = 0
    while a < interval_end:
        result += func(a) * precision
        a += precision
    return result


def f(x: float) -> float:
    return 2 * (1 - x * x) ** (1/2)


class AreaTest(unittest.TestCase):
    """Unit tests for area functions"""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples"""
        self.assertTrue(abs(area(f, -1, 1, 0.001) - 3.14) < 0.01)

