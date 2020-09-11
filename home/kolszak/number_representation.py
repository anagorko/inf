"""
Convert values between positional number systems.
"""

from typing import List

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def convert_to_dec(value: List[int], from_system: int) -> int:
    """Convert value from selected system to decimal."""
    value = value[::-1]
    result = 0
    for i in range(len(value)):
        result += value[i] * from_system ** i
    return result


def convert_from_dec(value: int, to_system: int) -> str:
    """Convert value from decimal to selected system."""
    result = ''
    while value > 0:
        result += digits[value % to_system]
        value //= to_system
    return result[::-1]

