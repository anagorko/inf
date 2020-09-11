"""
Recursive (a ** b) % m.
"""


def power(a: int, p: int, m: int) -> int:
    """Compute (a ** p) % m."""
    if p == 0:
        return 1
    if p % 2 == 1:
        return (a * pow(a * a, p // 2, m)) % m
    if p % 2 == 0:
        return pow(a * a, p // 2, m) % m
