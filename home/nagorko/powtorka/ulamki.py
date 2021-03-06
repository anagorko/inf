from fractions import Fraction
f = open("dane_ulamki.txt")
dane = []
for i in f:
    dane.append(list(map(int, i.rstrip("\n").split(" "))))
# print(dane)
print("____________65.1_____________")
skrocone = []
minimum = Fraction(1000, 1)
for i in dane:
    skrocone.append(Fraction(i[0], i[1]))
    if minimum > Fraction(i[0], i[1]):
        minimum = Fraction(i[0], i[1])
print(minimum)
same = []
for i in range(len(dane)):
    if skrocone[i] == minimum:
        same.append(dane[i])
print(same)

print("____________65.2_____________")
counter = 0
for i in range(len(dane)):
    if skrocone[i].denominator == dane[i][1] and skrocone[i].numerator == dane[i][0]:
        counter += 1
        # print(skrocone[i], dane[i])
print(counter)

print("____________65.3_____________")
suma = 0
for i in skrocone:
    suma += i.numerator
print(suma)

print("____________65.4_____________")
b = 4*9*25*49*13
suma = 0
for i in skrocone:
    suma += i.numerator*b/i.denominator
print(int(suma))
