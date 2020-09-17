"""
Merge sort implementation.
"""

import unittest
import timeit


def merge(first_list, second_list):
    result = []
    for n in range(len(first_list) + len(second_list)):
        if len(second_list) == 0:
            result.append(first_list[0])
            first_list.pop(0)
        elif len(first_list) == 0:
            result.append(second_list[0])
            second_list.pop(0)
        elif first_list[0] > second_list[0]:
            result.append(second_list[0])
            second_list.pop(0)
        else:
            result.append((first_list[0]))
            first_list.pop(0)
    return result


def merge_sort(list2sort):
    if len(list2sort) <= 1:
        return list2sort
    return merge(merge_sort(list2sort[0:len(list2sort) // 2]), merge_sort(list2sort[len(list2sort) // 2:]))


class NumberRepresentationTest(unittest.TestCase):
    """Unit tests for merge functions"""

    def test_handcrafted_examples(self):
        """Test some small hand picked examples"""
        self.assertEqual(merge([1, 2, 4, 5, 8], [2, 3, 6, 7]), [1, 2, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(merge_sort([1, 2, 4, 5, 8, 2, 3, 6, 7]), [1, 2, 2, 3, 4, 5, 6, 7, 8])


def benchmark():
    """Recursive vs iterative benchmark."""
    for n in range(1000):
        time_sorting = timeit.timeit(f'merge_sort.merge_sort(l)',
                    setup=f'import merge_sort\nimport random\n'f'l=[random.randint(1,1000) for _ in range({100*n})]',
                    number=1)

        print(f'n = {n}, iterative time: {time_sorting:.8f},')


if __name__ == '__main__':
    benchmark()
    print(merge_sort([2, 1, 45, 567, 2137, 543, 69, 420, 27, 21, 13, 1, 3, 5, 9, 17, 19, 21718281828, 31415, 16115,
                      3245634]))
