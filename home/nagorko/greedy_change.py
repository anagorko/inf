"""
Finds a minimal number of notes/coins needed to make a change. A greedy algorithm is used.
"""


from typing import Dict
import unittest

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def change(amount: int) -> Dict[int, int]:
    """Find how many coins of each denomination we need to get given amount.
    The total number of coins should be minimal."""
    changedict = {}
    while amount is not 0:
        for coin in reversed(COINS):
            if amount >= coin:
                changedict[coin] = amount // coin
                amount -= coin * changedict[coin]
    return changedict


class NumberRepresentationTest(unittest.TestCase):
    """Unit tests for num2sys functions"""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples"""
        self.assertEqual(change(44), {20: 2, 2: 2})


print(change(44))
