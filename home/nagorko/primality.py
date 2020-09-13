"""
Primality tests.
"""

import unittest
from typing import Set


def divisors(number: int) -> Set[int]:
    """Compute a set of all positive divisors of a given mumber"""

    if number == 0:
        return {0}
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            smaller_result = divisors(number // divisor)
            multiplied_result = {d * divisor for d in smaller_result}

            return smaller_result | multiplied_result
        divisor = divisor + 1

    return {1, number}


def prime(n: int) -> bool:
    """Test whether n is prime or not."""
    if len(divisors(n)) > 2 or n < 1:
        return False
    else:
        return True


def perfectd(n: int) -> bool:
    """Test whether n is perfect or not."""
    if sum(divisors(n)) - n == n:
        return True
    else:
        return False


class NumberRepresentationTest(unittest.TestCase):
    """Unit tests for num2sys functions"""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples"""
        for i in range(1000):
            self.assertEqual(perfectd(0), True)
            self.assertEqual(prime(0), False)
            self.assertEqual(prime(2), True)
            self.assertEqual(prime(7), True)
            self.assertEqual(prime(15), False)
            self.assertEqual(perfectd(6), True)
            self.assertEqual(perfectd(15), False)


print(perfectd(15))
