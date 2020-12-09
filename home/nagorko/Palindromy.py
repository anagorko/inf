import unittest


def create_pali_decimal():
    """Funkcja tworząca palindromy od 1 do 100000 w systemie dziesiętnym"""
    palindromy = []
    for i in range(1000):
        j = str(i)[::-1]
        palindromy.append(str(i)+j)
    for i in range(100):
        n = str(i)[::-1]
        for j in range(10):
            palindromy.append(str(i)+str(j)+n)
    for i in range(10):
        palindromy.append(str(i))
    return palindromy


def tnij(liczba, podstawa):
    """Funkcja zmieniająca na listę w wybranym systemie"""
    wynik = []
    while liczba > 0:
        wynik.append(liczba % podstawa)
        liczba = liczba // podstawa
    return rev_lista(wynik)


def rev_lista(lista):
    """Funkcja odwracająca listę"""
    wynik = []
    for i in range(len(lista)):
        wynik.append(lista[-i-1])
    return wynik


def policz_suma_pali():
    """Funkcja licząca sumę palindromów"""
    suma = 0
    for i in create_pali_decimal():
        i = int(i)
        if tnij(i, 10) == rev_lista(tnij(i, 10)) and tnij(i, 2) == rev_lista(tnij(i, 2)):
            suma += i
    return suma


class TestStringMethods(unittest.TestCase):
    def test_f1(self):
        self.assertEqual(tnij(4, 2), [1, 0, 0])

    def test_f2(self):
        self.assertEqual(rev_lista([1, 0, 0, 1]), [1, 0, 0, 1])

    def test_f3(self):
        self.assertEqual(policz_suma_pali(), 4)


print(policz_suma_pali())
