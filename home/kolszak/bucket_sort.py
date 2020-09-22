"""
Bucket sort.
"""
from typing import List
import random
import unittest


def bucket_sort(numbers: List[int], lowest: int, highest: int) -> List[int]:
    buckets = {i: 0 for i in range(lowest, highest + 1)}
    for num in numbers:
        buckets[num] += 1
    result = []
    for i in range(lowest, highest + 1):
        j = 0
        while j < buckets[i]:
            result.append(i)
            j += 1
    return result


class BucketSortTest(unittest.TestCase):
    """Unit tests for bucket sort functions"""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples"""
        self.assertEqual(bucket_sort([1, 2, 4, 5, 8, 2, 3, 6, 7], 0, 10000), [1, 2, 2, 3, 4, 5, 6, 7, 8])
