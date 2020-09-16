"""
Convert values between positional number systems.
"""

from typing import List
import unittest

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
digits_reverted = {'0': 0,
                   '1': 1,
                   '2': 2,
                   '3': 3,
                   '4': 4,
                   '5': 5,
                   '6': 6,
                   '7': 7,
                   '8': 8,
                   '9': 9,
                   'A': 10,
                   'B': 11,
                   'C': 12,
                   'D': 13,
                   'E': 14,
                   'F': 15}


def _convert_to_dec(value: List[int], from_system: int) -> int:
    """Convert value from selected system to decimal."""
    value = value[::-1]
    result = 0
    for i in range(len(value)):
        result += value[i] * from_system ** i
    return result


def _convert_from_dec(value: int, to_system: int) -> List[int]:
    """Convert value from decimal to selected system."""
    result = []
    while value > 0:
        result.append(value % to_system)
        value //= to_system
    return result[::-1]


def convert(value: str, from_system: int, to_system: int) -> str:
    v = []
    for c in value:
        v.append(digits_reverted[c])
    r = _convert_from_dec(_convert_to_dec(v, from_system), to_system)
    r_str = ''
    for i in range(len(r)):
        r_str += digits[r[i]]
    return r_str


class ConvertBetweenPositionalNumberSystemsTests(unittest.TestCase):
    """Unit tests for positional systems conversion functions."""

    def test_convert(self):
        """Test some small hand picked example."""
        self.assertEqual(convert('254', 10, 16), 'FE')

