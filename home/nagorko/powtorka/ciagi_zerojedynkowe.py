f = open("ciagi.txt")
dane = []

for i in f:
    dane.append(i.rstrip("\n"))

# print(dane)

print("_____________63.1____________")
for i in dane:
    dlugosc = len(i)
    if dlugosc % 2 == 0:
        dlugosc = dlugosc // 2
        if i[0:dlugosc] == i[dlugosc:]:
            print(i)
print("_____________63.2____________")
counter = 0
for i in dane:
    for j in range(len(i)-1):
        if i[j] == "1" and i[j+1] == "1":
            counter += -1
            break
    counter += 1
print(counter)
print("____________63.3______________")


def czynniki_pierwsze(x):
    y = x
    result = []
    i = 2
    while x % i == 0:
        x = x // i
        result.append(i)
    i = 3
    while i**2 < y:
        while x % i == 0:
            x = x // i
            result.append(i)
        i += 2
    if y % x == 0 and x != 1:
        result.append(x)
    return result


# print(czynniki_pierwsze(126))
counter = 0
minimal = 10000000
maximal = 0
for i in dane:
    if len(czynniki_pierwsze(int(i, 2))) == 2:
        counter += 1
        if maximal < int(i, 2):
            maximal = int(i, 2)
        if minimal > int(i, 2):
            minimal = int(i, 2)
print(counter, maximal, minimal)
print(czynniki_pierwsze(maximal), czynniki_pierwsze(minimal))
