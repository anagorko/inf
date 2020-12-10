"""Palindromes"""

import unittest
import random


def digits(num, divisor):       # divisor is based on numeral system in which the given number is to be represented
    """Converts a number into a list of separate digits"""
    bin_list = []

    if num == 0:
        return [0]

    while num > 0:
        bin_list.append(num % divisor)
        num = num // divisor

    bin_list_final = []

    i = 1
    for _ in bin_list:
        bin_list_final.append(bin_list[-i])
        i += 1

    return bin_list_final


def is_palindrome(num, system):
    """Checks whether a given number is a palindrome. Providing numeral system of the number is required."""
    num_list = digits(num, system)
    state = True

    index = 1
    for element in num_list:
        if element != num_list[-index]:
            state = False
        index += 1

    return state


def sum_palindrome(ran):
    """Sums all the palindromes in a given range"""
    final_sum = 0

    for num in range(ran):
        if is_palindrome(num, 2) and is_palindrome(num, 10):
            final_sum += num

    return final_sum


print(sum_palindrome(10**6))


class PalindromeTest(unittest.TestCase):
    """Tests out programme"""

    def test_digits(self):
        """Tests our <digits> function comparing results of operations on pseudo-randomly generated numbers with those
           from pre-built functions"""

        for test_case in range(0, 10000):
            num = random.choice(range(10000))

            self.assertEqual(digits(num, 10), [int(digit) for digit in str(num)])

            binary_num = bin(num)
            binary_num = int(binary_num[2:])
            self.assertEqual(digits(num, 2), [int(digit) for digit in str(binary_num)])


# The rest of the functions are, in my opinion, too simple to become a subject of a test


if __name__ == '__main__':

    unittest.main()
