ZERO = 48
A = 65

def decToAny(dec, any):
    r = dec % any
    if dec - r == 0:
        return char(r)
    return decToAny((dec - r) // any, any) + char(r)

def char(r):
    if r < 10:
        return chr(ZERO + r)
    return chr(A + r - 10)

def anyToDec(num, any):
    mn = 1
    cf = str(num)
    sum = 0
    licznik = 0
    while licznik < len(cf):
        a = 0
        if ord(cf[licznik]) < A:
            a = ord(cf[licznik]) - ZERO
        else:
            a = ord(cf[licznik]) - A + 10

        sum = sum + a * mn
        licznik = licznik + 1
        mn = mn * any
    return sum

def anyToAny(num, rep, any):
    return decToAny(anyToDec(num, rep), any)


print(decToAny(10, 2))
print(anyToDec('0101', 2))
print(anyToAny('0101', 2, 10))
print(anyToAny('01', 10, 10))
print(anyToDec('0H', 18))
print(17*18)
print(anyToAny('01', 15, 16))
print(anyToAny('01', 16, 17))
print(anyToAny('A1', 16, 17))

"""
print(anyToDec(decToAny(10, 2), 2))
print(decToAny(10, 4))
print(anyToDec(decToAny(10, 4), 4))
print(decToAny(10, 8))
print(anyToDec(decToAny(10, 8), 8))
print(decToAny(10, 16))
print(anyToDec(decToAny(10, 16), 16))
print(decToAny(17, 18))
print(anyToDec(decToAny(17, 18), 18))
"""
