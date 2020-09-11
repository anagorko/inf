"""
Iterative and recursive computation of GCD (greatest common divisor), using Euclid's algorithm.
"""


def gcd_iter(a: int, b: int) -> int:
    """Compute greatest common divisor of a and b, recursive version."""
    while b is not 0:
        c = a % b
        a = b
        b = c
    return a

def gcd_rec(a: int, b: int) -> int:
    """Compute greatest common divisor of a and b, iterative version."""
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)
    
print(gcd_rec(12,15))
