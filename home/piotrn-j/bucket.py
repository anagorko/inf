"""
Bucket sort
"""

import random
import unittest


def bucket_sort(given_list, lowest, highest):
    """Bucket sort algorithm implementation"""

    result = [0 for _ in range(highest - lowest + 1)]
    result_final = []

    for element in given_list:
        result[element - lowest] += 1

    index = 0

    for element in result:
        for n in range(element):
            result_final.append(lowest + index)
        index += 1

    return result_final


class BucketSortTest(unittest.TestCase):
    """Test"""

    def test_bucket_sort(self):
        """Test"""

        for n in range(0, 100):
            random_list = random.choices(range(10000), k=1000)
            testlist = random_list
            random_list.sort()
            self.assertEqual(random_list, bucket_sort(testlist, 0, 10000))


if __name__ == '__main__':
    unittest.main()
