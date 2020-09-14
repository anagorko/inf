"""
kod do zadania pseudo_random, przekracza limity czasowe
treść:
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=286
"""
from sys import stdin


def generate_sequence(z, i, m, l):
    sequence = {l}
    counter = 1
    while True:
        l = (z*l+i) % m
        if l in sequence:
            return counter
        else:
            sequence.add(l)
            counter += 1


count = 1
while stdin:
    wejscie = list(map(int, input().split()))
    if wejscie == [0, 0, 0, 0]:
        break
    print("Case ", count, ": ", generate_sequence(wejscie[0], wejscie[1], wejscie[2], wejscie[3]))
    count += 1

