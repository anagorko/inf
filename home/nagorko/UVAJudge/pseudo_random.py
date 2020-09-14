"""
kod do zadania pseudo_random, przekracza limity czasowe
"""
from sys import stdin


def is_in_sequence(a, b):
    for i in a:
        if i == b:
            return True
    return False


def generate_sequence(z, i, m, l):
    sequence = [l]
    counter = 1
    while True:
        l = (z*l+i) % m
        if is_in_sequence(sequence, l):
            return counter
        else:
            sequence.append(l)
            counter += 1


count = 1
while stdin:
    wejscie = list(map(int, input().split()))
    print("Case ", count, ": ", generate_sequence(wejscie[0], wejscie[1], wejscie[2], wejscie[3]))
    count += 1
