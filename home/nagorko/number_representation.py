"""
Number system conversions: dec, hex and bin bases.
"""

import unittest

string2num = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0,
              1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0",
              "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
              10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
              }


def int2dec(n: int) -> str:
    """Convert an integer to a string in decimal number system."""
    result = ""
    if n == 0:
        result = "0"
    while n is not 0:
        result = string2num[n % 10] + result
        n = n // 10
    return result


def int2bin(n: int) -> str:
    """Convert an integer to a string in binary number system."""
    result = ""
    if n == 0:
        result = "0"
    while n is not 0:
        result = string2num[n % 2] + result
        n = n // 2
    return result


def int2hex(n: int) -> str:
    """Convert an integer to a string in hexadecimal number system."""
    divisor = 16
    result = ""
    if n == 0:
        result = "0"
    while n is not 0:
        result = string2num[n % divisor] + result
        n = n // divisor
    return result


def dec2int(r: str) -> int:
    """Convert a decimal representation to an int."""
    result = 0
    divisor = 10
    score = 1
    for i in reversed(r):
        result += string2num[i]*divisor**score
        score += 1
    return result // divisor


def bin2int(r: str) -> int:
    """Convert a binary representation to an int."""
    result = 0
    divisor = 2
    score = 1
    for i in reversed(r):
        result += string2num[i] * divisor ** score
        score += 1
    return result // divisor


def hex2int(r: str) -> int:
    """Convert a hexadecimal representation to an int."""
    result = 0
    divisor = 10
    score = 1
    for i in reversed(r):
        result += string2num[i] * divisor ** score
        score += 1
    return result // divisor


class NumberRepresentationTest(unittest.TestCase):
    """Unit tests for num2sys functions"""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples"""
        for i in range(1000):
            self.assertEqual(int2dec(i), str(i))
            self.assertEqual(dec2int(str(i)), i)


if __name__ == '__main__':
    print(dec2int("2"))
    print(int2hex(0))
