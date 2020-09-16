import unittest


def greedy_change(income):
    coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    change = []
    for x in coins:
        if x <= income:
            change.append(income//x)
        else:
            change.append(0)
        income = income % x
    dictionary = {nominal: number for nominal, number in zip(coins, change)}

    return dictionary


class DivisorTest(unittest.TestCase):
    """Unit tests for greedy change."""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples."""
        self.assertDictEqual(greedy_change(44), {500: 0, 200: 0, 100: 0, 50: 0, 20: 2, 10: 0, 5: 0, 2: 2, 1: 0})


print(greedy_change(44))
