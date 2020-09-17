
from typing import List


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


def sort_recursive(a: List[int]) -> List[int]:
    if len(a) == 1:
        return a
    else:
        a1 = sort_recursive(a[:len(a) // 2])
        a2 = sort_recursive(a[len(a) // 2:])
        return merge(a1, a2)

