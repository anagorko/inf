
def generujLiczbyPierwszeDo(num):
    liczbypierwsze = [2]
    for i in range(3, num + 1):
        tak = True
        for liczna in liczbypierwsze:
            if i % liczna == 0:
                tak = False
                break
        if tak:
            liczbypierwsze.append(i)
    return liczbypierwsze


def isPrimary(num):
    lp = generujLiczbyPierwszeDo(int(num ** (1/2)))
    for numer in lp:
        if num % numer == 0:
            return False
    return True

def decimalsOfNumber(num):
    dec = [1]
    for i in range(2, num):
        if num % i == 0:
            dec.append(i)
    return dec


def isIdeal(num):
    dz = decimalsOfNumber(num)
    suma = 0
    for dzielnik in dz:
        suma = suma + dzielnik
    if suma == num:
        return True
    return False

print(isPrimary(10000))
print(isIdeal(6))
print(isIdeal(28))
print(isIdeal(496))
print(isIdeal(8128))
print(isIdeal(10))
print(isIdeal(666))
print(isIdeal(2137))