"""
Numeral systems converter
"""

import unittest
import random


def dec_to_bin(num):
    """Converts a decimal number into a binary one."""

    if num == 0:
        return '0b0'

    rem_list = []

    while num != 0:
        remainder = num % 2
        rem_list.append(remainder)
        num = num // 2

    rem_list.reverse()

    result = [str(digit) for digit in rem_list]
    result = "".join(result)

    return '0b' + result


def bin_to_dec(num):
    """Converts a binary number into a decimal one"""

    num = int(num[2:])

    power = len(str(num))
    result = 0
    temp_list = [int(n) for n in str(num)]

    for i in range(1, len(str(num)) + 1):
        power = power - 1
        result = result + temp_list[i - 1] * 2 ** power

    return result


def dec_to_hex(num):
    """Converts a decimal number into a hexadecimal one"""

    result = []
    rem_list = []

    while num != 0:
        remainder = num % 16
        rem_list.append(remainder)
        num = num // 16

    rem_list.reverse()

    hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]

    for digit in rem_list:
        result.append(str(hex_list[digit]))

    result = "".join(result)

    return '0x' + result


def bin_to_hex(num):
    """Converts a binary number into a hexadecimal one"""

    num = int(num[2:])

    num_list = [int(n) for n in str(num)]
    index = 0
    four_digits = []
    hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]
    bin_list = [str(dec_to_bin(n)[2:]) for n in range(0, 16)]
    result = []

    for number in bin_list:
        while len(number) < 4:
            number = '0' + number
            bin_list[index] = number
        index = index + 1

    index = 0

    while len(num_list) % 4 != 0:
        num_list[:0] = [0]

    for digit in num_list:
        four_digits.append(str(digit))
        index = index + 1

        if index == 4:
            result.append(str(hex_list[bin_list.index("".join(four_digits))]))
            index = 0
            four_digits = []

    return '0x' + "".join(result)


def hex_to_dec(num):
    """Converts a hexadecimal number into a decimal one"""

    num = num[2:]
    power = len(num)
    result = 0
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "a", "b", "c", "d", "e", "f"]
    temp_list = [n for n in num]
    index = 0

    for number in temp_list:
        number = hex_list.index(number)
        temp_list[index] = int(number)
        index = index + 1

    for i in range(1, len(str(num)) + 1):
        power = power - 1
        result = result + temp_list[i - 1] * 16 ** power

    return int(result)


def hex_to_bin(num):
    """Converts a hexadecimal number into a binary one"""

    num = num[2:]

    num_list = [n for n in num]
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', "a", "b", "c", "d", "e", "f"]
    bin_list = [dec_to_bin(n)[2:] for n in range(0, 16)]
    result = []
    index = 0

    for number in bin_list:
        while len(number) < 4:
            number = '0' + number
            bin_list[index] = number
        index = index + 1

    index = 0

    for number in num_list:
        number = hex_list.index(number)
        num_list[index] = int(number)
        index = index + 1

    for n in num_list:
        result.append(bin_list[n])

    result = "".join(result)

    for n in result:
        if n == '0':
            result = result[1:]
        else:
            break

    return '0b' + result


class NumeralConverterTest(unittest.TestCase):
    """Set of tests for this whole programme"""

    def test_compare_with_builtin_functions(self):
        """The test compares results from this programme with those provided by built-in functions"""

        for n in range(0, 100000):
            num = random.choices(range(0, 10 ** 9), k=1)
            num = num[0]

            self.assertEqual(bin(num), dec_to_bin(num))
            self.assertEqual(hex(num), dec_to_hex(num))

            num = bin(num)

            self.assertEqual(int(num, 2), bin_to_dec(num))
            self.assertEqual(hex(int(num, 2)), bin_to_hex(num))

            num = hex(int(num, 2))

            self.assertEqual(int(num, 16), hex_to_dec(num))
            self.assertEqual(bin(int(num, 16)), hex_to_bin(num))


if __name__ == '__main__':
    unittest.main()
