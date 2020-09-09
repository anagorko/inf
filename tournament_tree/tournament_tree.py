"""
Tournament tree implementation.
"""

import abc
import unittest


class TournamentTree(abc.ABC):
    def __init__(self):
        """Initialization of data structures."""

    @abc.abstractmethod
    def increment(self, a: int, b: int):
        """Increment all counters in closed interval [a, b]."""

    @abc.abstractmethod
    def decrement(self, a: int, b: int):
        """Decrement all counters in closed interval [a, b]."""

    @abc.abstractmethod
    def max(self) -> int:
        """Return maximal value of a counter."""


class BruteForce(TournamentTree):
    """Brute force implementation of TournamentTree."""

    def __init__(self):
        super().__init__()

        self.counters = dict()

    def increment(self, a: int, b: int):
        for i in range(a, b+1):
            self.counters[i] = self.counters.get(i, 0) + 1

    def decrement(self, a: int, b: int):
        for i in range(a, b+1):
            self.counters[i] = self.counters.get(i, 0) - 1

    def max(self):
        return max(self.counters.values())


class Optimized(TournamentTree):
    """Optimized implementation of TournamentTree."""


class TournamentTreeUnitTest(unittest.TestCase):
    def test_brute_force(self):
        tt = BruteForce()
        tt.increment(1, 3)
        tt.increment(3, 5)
        tt.increment(2, 3)
        self.assertEqual(tt.max(), 3)


def main():
    tt = BruteForce()
    tt.increment(1, 3)
    tt.increment(3, 5)
    tt.increment(2, 3)

    print(tt.counters)


if __name__ == '__main__':
    main()
