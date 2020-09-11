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

    def __init__(self, maxsize: int):
        n : int = 2

        while n<maxsize:
            n = n * 2

        self.maxsize : int = maxsize
        self.maximum : int = 0
        self.N : int = n
        self.tree = [0] * (n*2 + 1)
        self.maximumtree = [0] * (n*2 + 1)
        self.needcompute = [False] * (n*2 + 1)
        
    def _addUp(self, x : int):
        self.needcompute[x] = True
        while x > 1:
            x = x // 2
            self.needcompute[x] = True
    
    def increment(self, a: int, b: int, wartosc : int = 1):
        x : int = self.N + a
        y : int = self.N + b

        self.tree[x] = self.tree[x] + wartosc
        self._addUp(x)
        if x != y:
            self.tree[y] = self.tree[y] + wartosc
            self._addUp(y)

        while x // 2 != y // 2:
            if x % 2 == 0:
                self.tree[x+1] = self.tree[x+1] + wartosc
                self._addUp(x+1)
            if y % 2 == 1:
                self.tree[y - 1] = self.tree[y-1] + wartosc
                self._addUp(y-1)
                
            x = x // 2
            y = y // 2

    def decrement(self, a: int, b: int, wartosc : int = 1):
        x : int = self.N + a
        y : int = self.N + b

        self.tree[x] = self.tree[x] - wartosc
        self._addUp(x)
        if x != y:
            self.tree[y] = self.tree[y] - wartosc
            self._addUp(y)

        while x // 2 != y // 2:
            if x % 2 == 0:
                self.tree[x+1] = self.tree[x+1] - wartosc
                self._addUp(x+1)
            if y % 2 == 1:
                self.tree[y - 1] = self.tree[y-1] - wartosc
                self._addUp(y-1)
                
            x = x // 2
            y = y // 2

    def max(self, x : int = 1):
        if x >= self.N:
            return self.tree[x]
        if not self.needcompute[x]:
            return self.maximumtree[x]
            
        self.needcompute[x] = False
        self.maximumtree[x] = max(self.max(x*2), self.max(x*2 + 1)) + self.tree[x]
        return self.maximumtree[x]

class TournamentTreeUnitTest(unittest.TestCase):
    def test_brute_force(self):
        tt = BruteForce()
        tt.increment(1, 3)
        tt.increment(3, 5)
        tt.increment(2, 3)
        self.assertEqual(tt.max(), 3)
    def test_optimal_tree(self):
        tb = BruteForce()
        to = Optimized(100)

        for i in range(100):
            for j in range(i, 100):
                tb.increment(i, j)
                to.increment(i, j)
                self.assertEqual(tb.max(), to.max())
        for i in range(100):
            for j in range(i, 100):
                tb.decrement(i, j)
                to.decrement(i, j)
                self.assertEqual(tb.max(), to.max())


def main():
    print("tak")


if __name__ == '__main__':
    main()
