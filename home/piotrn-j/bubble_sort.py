"""
Bubble sort
"""

import unittest
import random


def bubble_sort(given_list):
    """Sorts given list of numbers from the smallest to the biggest value"""

    index = 1

    for n in range(len(given_list)):
        for number in given_list:
            if index != len(given_list):
                if number > given_list[index]:
                    given_list[index - 1] = given_list[index]
                    given_list[index] = number
            index = index + 1
        index = 1

    return given_list


class BubbleSortTest(unittest.TestCase):
    """Test"""

    def test_bubble_sort(self):
        """Test"""

        for n in range(0, 100):
            random_list = random.choices(range(0, 10000), k=1000)
            testlist = random_list
            random_list.sort()
            self.assertEqual(random_list, bubble_sort(testlist))


if __name__ == '__main__':
    unittest.main()
