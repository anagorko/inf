"""
Iterative and recursive computation of nth Fibonacci number.
"""

import unittest
import timeit


def iterative(n: int) -> int:
    """Compute nth Fibonacci number. Iterative version."""

    f = [1, 1]

    for i in range(n - 2):
        f.append(f[-1] + f[-2])

    return f[-1]


def recursive(n: int) -> int:
    """Compute nth Fibonacci number. Recursive version."""

    if n <= 2:
        return 1

    return recursive(n-1) + recursive(n-2)


class FibonacciTest(unittest.TestCase):
    """Unit tests for mod_power functions"""

    def test_handcrafted_examples(self):
        self.assertEqual(iterative(3), 2)
        self.assertEqual(recursive(4), 3)
        self.assertEqual(iterative(5), 5)
        self.assertEqual(recursive(6), 8)

    def test_iterative_vs_recursive(self):
        for n in range(10):
            self.assertEqual(iterative(n), recursive(n))


def main():
    for n in range(100):
        time_iterative = timeit.timeit(f'fibonacci.iterative({n})', setup='import fibonacci', number=1)
        time_recursive = timeit.timeit(f'fibonacci.recursive({n})', setup='import fibonacci', number=1)
        print(f'n = {n}, iterative time: {time_iterative:.8f}, recursive time: {time_recursive:.8f}')


if __name__ == '__main__':
    main()
