"""
Greatest common divisor
"""

import unittest
import random
import math


def gcd_rec(a, b):
    """Recursive method of finding the GCD of given two numbers using Euclidean algorithm"""

    if a == 0:
        return b
    elif b == 0:
        return a

    if a != b:
        if a > b:
            a = a - b
            return gcd_rec(a, b)
        elif a < b:
            b = b - a
            return gcd_rec(a, b)
    else:
        return a


def gcd_it(a, b):
    """Iterative method of finding the GDC of given two number using Euclidean algorithm"""

    if a == 0:
        return b
    elif b == 0:
        return a

    a = a
    b = b

    while a != b:
        if a > b:
            a = a - b
        elif a < b:
            b = b - a

    return a


class GcdTest(unittest.TestCase):
    """Set of tests for this whole programme"""

    def test_random_examples(self):
        """Test a thousand examples for random numbers between 0 and 10^3 using built-in Python function"""

        for n in range(0, 1000):
            num1 = random.choices(range(0, 10 ** 3), k=1)
            num2 = random.choices(range(0, 10 ** 3), k=1)

            self.assertEqual(gcd_it(num1[0], num2[0]), math.gcd(num1[0], num2[0]))
            self.assertEqual(gcd_rec(num1[0], num2[0]), math.gcd(num1[0], num2[0]))

    # Repeated tests have proven that iterative method is far more practical than recursive one, as if range for random
    #   numbers exceeds 10 000, the programme is very likely to meet the maximum depth of recursion and return error.

    # The author of this code conducted about ten million tests for iterative method using numbers between 1 and
    #   a billion, because he wanted to heat up his room a little. What he did not know though, was that PyCharm will
    #   not use more than 25% of CPU's computing power, because it can only run on one core.


if __name__ == '__main__':
    unittest.main()
