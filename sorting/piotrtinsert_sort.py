"""
Lekcja informatyki 16.09.2020
Sortowanie przez Wstawianie

"""

def InsertSort(tab):
    minimum = float('-inf')
    r = []
    index = 0

    for i in tab:
        localminumim = float('inf')
        for numer in tab:
            if numer < localminumim and numer > minimum:
                localminumim = numer
        for numer in tab:
            if numer == localminumim:
                r.append(localminumim)
        minimum = localminumim
    return r

print(InsertSort([0, 1, 4, 9, 1, 2, 3, 4, 5, 90, 98, 79, 63, 3, 0]))

