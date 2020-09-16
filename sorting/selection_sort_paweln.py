"""
Selection sort implementation.
"""

from typing import List, Tuple
import timeit


def get_max(integers: List[int]) -> int:
    max_ = integers[0]
    for i in integers:
        if i > max_:
            max_ = i
    return max_


def get_min(integers: List[int]) -> int:
    min_ = integers[0]
    for i in integers:
        if i < min_:
            min_ = i
    return min_


def selection_sort(a):
    result = []
    for i in range(len(a)):
        result.append(get_min(a))
        a.remove(get_min(a))
    return result


def benchmark():
    time_selectionsort = timeit.timeit('selection_sort.selection_sort(l)', setup='import selection_sort\nimport random\n''l=[random.randint(1,1000) for _ in range(10000)]', number=1000)
    print(f'time {time_selectionsort} ')


if __name__ == '__main__':
    benchmark()
    print(selection_sort([2, 1, 45, 567, 2137, 543, 69, 420, 27, 21, 13, 1, 3, 5, 9, 17, 19, 21718281828]))
