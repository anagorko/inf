"""
Finds a minimal number of notes/coins needed to make a change. A greedy algorithm is used.
"""


from typing import Dict


COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def change(amount: int) -> Dict[int, int]:
    """Find how many coins of each denomination we need to get given amount.
    The total number of coins should be minimal."""
    chang = {1 : 0, 2: 0, 5 : 0, 10 : 0, 20 : 0, 50 : 0, 100 : 0, 200 : 0}
    licznik = 7
    while licznik >= 0:
        while amount - COINS[licznik] >= 0:
            chang[COINS[licznik]] = chang[COINS[licznik]] + 1
            amount = amount - COINS[licznik]
        licznik = licznik - 1
    return chang

print(change(2137))
