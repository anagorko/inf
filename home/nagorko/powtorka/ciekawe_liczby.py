f = open("liczby1.txt")
e = open("liczby2.txt")
dane1 = []
dane2 = []
for i in f:
    dane1.append(i.rstrip("\n"))
for i in e:
    dane2.append(i.rstrip("\n"))
# print(dane1)
# print(dane2)
print("_______62.1_______")
max_counter = 0
min_counter = 10000
for i in dane1:
    if int(i) > max_counter:
        max_counter = int(i)
    if int(i) < min_counter:
        min_counter = int(i)
print(max_counter, min_counter)
print("_______62.2_______")
"""lista nie sprawdza ostatniej liczby ale dla tych danych nie ma to znaczenia"""
ciagi = []
for i in range(len(dane1)):
    last = int(dane1[i])
    res = [dane1[i]]
    dlugosc_ciagu = 1
    if i + 1 == len(dane1):
        break
    while last <= int(dane1[i+1]):
        dlugosc_ciagu += 1
        last = int(dane1[i+1])
        i += 1
        if i + 1 == len(dane1):
            break
    res.append(dlugosc_ciagu)
    ciagi.append(res)
ciagi.append(["100556", 1])
# print(ciagi)
max_counter = 0
res = []
for i in ciagi:
    if i[1] > max_counter:
        max_counter = i[1]
        res = i
print(res)
print("_________62.3_________")


def oct_to_dec(x):
    result = 0
    for j in range(len(x)):
        result += 8**(len(x)-j-1)*int(x[j])
    return result


def dec_to_oct(x):
    result = ""
    x = int(x)
    while x > 0:
        result += str(x % 8)
        x = x // 8
    return result[::-1]


# print(oct_to_dec("22666"))
# print(dec_to_oct("9654"))
wynik = [0, 0]
for i in range(len(dane1)):
    if oct_to_dec(dane1[i]) == int(dane2[i]):
        wynik[0] += 1
    if oct_to_dec(dane1[i]) > int(dane2[i]):
        wynik[1] += 1
print(wynik)
print("_________62.4_________")
counter = 0
counter2 = 0
for i in dane2:
    for j in i:
        if j == "6":
            counter += 1
    for j in dec_to_oct(i):
        if j == "6":
            counter2 += 1
print(counter, counter2)
