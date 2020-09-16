"""
Iterative and recursive computation of nth Fibonacci number.
"""

import unittest
import timeit


def iterative(n: int) -> int:
    """Compute nth Fibonacci number. Iterative version."""

    sequence = [1, 1]

    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence[-1]


def recursive(n: int) -> int:
    """Compute nth Fibonacci number. Recursive version."""

    if n <= 2:
        return 1

    return recursive(n-1) + recursive(n-2)


class FibonacciTest(unittest.TestCase):
    """Unit tests for mod_power functions"""

    def test_handcrafted_examples(self):
        """Some hand crafted tests."""
        self.assertEqual(iterative(3), 2)
        self.assertEqual(recursive(4), 3)
        self.assertEqual(iterative(5), 5)
        self.assertEqual(recursive(6), 8)

    def test_iterative_vs_recursive(self):
        """Compare iterative and recursive versions."""
        for n in range(20):
            self.assertEqual(iterative(n), recursive(n))


def benchmark():
    """Recursive vs iterative benchmark."""
    for n in range(100):
        time_iterative = timeit.timeit(f'fibonacci.iterative({n})', setup='import fibonacci',
                                       number=1)
        time_recursive = timeit.timeit(f'fibonacci.recursive({n})', setup='import fibonacci',
                                       number=1)
        print(f'n = {n}, iterative time: {time_iterative:.8f}, recursive time:'
              f'{time_recursive:.8f}')


if __name__ == '__main__':
    benchmark()
