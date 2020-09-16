"""
Finds minimal number of coins needed to make a change using greedy algorithm.
"""

import unittest
from typing import Dict

coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def change(amount: int) -> Dict[int, int]:
    result = {}
    for i in range(len(coins)):
        result[coins[i]] = 0
        while amount >= coins[i]:
            amount -= coins[i]
            result[coins[i]] += 1
    return result


class GreedyChangeTest(unittest.TestCase):
    """Change function tests."""

    def test_change_test(self):
        """Test some small hand picked example."""
        self.assertEqual(change(1423), {500: 2, 200: 2, 100: 0, 50: 0, 20: 1, 10: 0, 5: 0, 2: 1, 1: 1})

