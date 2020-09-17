"""
Merge sort.
"""

from typing import List
import unittest
import timeit
import random


def merge(a: List[int], b: List[int]) -> List[int]:
    result = []
    i, j = 0, 0
    while i < len(a) or j < len(b):
        while j < len(b) and (i >= len(a) or b[j] <= a[i]):
            result.append(b[j])
            j += 1
        while i < len(a) and (j >= len(b) or a[i] <= b[j]):
            result.append(a[i])
            i += 1

    return result


def merge_sort(a: List[int]) -> List[int]:
    if len(a) == 1:
        return a
    else:
        a1 = merge_sort(a[:len(a) // 2])
        a2 = merge_sort(a[len(a) // 2:])
        return merge(a1, a2)


class MergeTest(unittest.TestCase):
    """Unit tests for merge functions"""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples"""
        self.assertEqual(merge([1, 2, 4, 5, 8], [2, 3, 6, 7]), [1, 2, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(merge_sort([1, 2, 4, 5, 8, 2, 3, 6, 7]), [1, 2, 2, 3, 4, 5, 6, 7, 8])


def benchmark():
    """Benchmark."""
    for n in range(10000):
        a = [random.randint(-1000, 1000) for i in range(10)]
        time_ = timeit.timeit(f'merge_sort.merge_sort({a})', setup='import merge_sort', number=1)
        print(f'input = {a}, time: {time_:.8f}')
        print(f'output = {merge_sort(a)}')


if __name__ == '__main__':
    benchmark()
