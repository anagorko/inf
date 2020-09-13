"""
Finds a minimal number of notes/coins needed to make a change. A greedy algorithm is used.
"""


from typing import Dict


COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def change(amount: int) -> Dict[int, int]:
    """Find how many coins of each denomination we need to get given amount.
    The total number of coins should be minimal."""
