"""
Lekcja informatyki 16.09.2020
Sortowanie przez Scalanie

"""

import unittest
import timeit
import random

def Merge(a, b):
    """scala dwa fragmenty"""
    r = []
    a.append(float('inf'))
    b.append(float('inf'))
    i = iter(a)
    j = iter(b)
    n = next(i)
    m = next(j)

    while n != float('inf') or m != float('inf'):
        if n < m:
            r.append(n)
            n = next(i)
        else:
            r.append(m)
            m = next(j)
    return r

def MergeSort(tab):
    """Zwraca posortowaną tablicę podaną na wejściu"""
    if len(tab) > 1:
        return Merge(MergeSort(tab[:len(tab)//2]), MergeSort(tab[len(tab)//2:]))
    return tab


def BubbleSort(tab):
    for a in range(len(tab)):
        for i in range(len(tab) - 1):
            if tab[i + 1] < tab[i]:
                c = tab[i]
                tab[i] = tab[i + 1]
                tab[i + 1] = c
    return tab

class MergeSortTest(unittest.TestCase):
    """Unit test na poprawność działania"""
    def test_handcrafted_examples(self):
        a = [0, 1, 4, 9, 1, 2, 3, 4, 5, 90, 98, 79, 63, 3, 0]
        b = [0, 0, 1, 1, 2, 3, 3, 4, 4, 5, 9, 63, 79, 90, 98]
        self.assertEqual(MergeSort(a), b)

    def test_mergesort_vs_bublesort(self):
        """Compare iterative and recursive versions."""
        for m in range(100):
            a = []
            for n in range(100):
                a.append(random.randint(0, 1000000))
            self.assertEqual(MergeSort(a), BubbleSort(a))

def benchmark():
    """iterative vs recursive benchmark."""
    for m in range(1000, 10000):
        a = []
        if m % 500 == 0:
            for n in range(m + 1):
                a.append(random.randint(0, 1000000))

            time_iterative = timeit.timeit(f'merge_sort.BubbleSort({a})', setup='import merge_sort',
                                        number=1)
            time_recursive = timeit.timeit(f'merge_sort.MergeSort({a})', setup='import merge_sort',
                                        number=1)
            print(f'n = {m}, iterative time: {time_iterative:.8f}, recursive time:'
                f'{time_recursive:.8f}')

if __name__ == '__main__':
    benchmark()