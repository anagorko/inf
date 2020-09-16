"""
Lekcja informatyki 16.09.2020
Sortowanie Bąbelkowe

"""

def BubbleSort(tab):
    for a in range(len(tab)):
        for i in range(len(tab) - 1):
            if tab[i + 1] < tab[i]:
                c = tab[i]
                tab[i] = tab[i + 1]
                tab[i + 1] = c
    return tab

print(BubbleSort([0, 1, 4, 9, 1, 2, 3, 4, 5, 90, 98, 79, 63, 3, 0]))