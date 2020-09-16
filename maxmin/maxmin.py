"""
Find minimal and maximal element in a list.
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


def naive(integers: List[int]) -> Tuple[int, int]:
    return get_max(integers), get_min(integers)


def optimized(integers: List[int]) -> Tuple[int, int]:
    """Find maximal and minimal element in a list."""

    assert(integers)

    max_ = integers[0]
    min_ = integers[0]

    for i in integers:
        if i > max_:
            max_ = i
        elif i < min_:
            min_ = i

    return max_, min_


def benchmark():
    time_naive = timeit.timeit('maxmin.naive(l)', setup='import maxmin\nimport random\nl=[random.randint(1,1000) for _ in range(10000)]', number=1000)
    time_optimized = timeit.timeit('maxmin.optimized(l)', setup='import maxmin\nimport random\nl=[random.randint(1,1000) for _ in range(10000)]', number=1000)
    print(f'naive time {time_naive} optimized time {time_optimized}')


if __name__ == '__main__':
    benchmark()