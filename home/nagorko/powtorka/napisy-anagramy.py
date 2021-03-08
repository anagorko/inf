from collections import Counter
f = open("dane_napisy.txt")
dane = []
dane2 = []
dane3 = []
for i in f:
    for x in i.rstrip("\n").split(" "):
        dane3.append(x)
    dane.append(list(map(sorted, i.rstrip("\n").split(" "))))
    dane2.append(list(map(set, i.rstrip("\n").split(" "))))
    j = list(map(sorted, i.rstrip("\n").split(" ")))

# print(dane3)

counter = 0
print("__________68.1_________")
""" testowe przykłady to linia 972 [nie] i 982 [tak]"""
for i in range(len(dane)):
    if len(dane2[i][0]) == 1 and dane[i][0] == dane[i][1]:
        counter += 1
print(counter)

counter = 0
print("__________68.2_________")
for i in dane:
    if i[0] == i[1]:
        counter += 1
print(counter)

maximum = 0
counter = 0
print("__________68.3_________")
# print(Counter(dane3).most_common(1))

data = []
for i in dane:
    data.append(i[0])
    data.append(i[1])
data = sorted(data)

counter = 0
napis = ""
for i in data:
    if data.count(i) > counter:
        counter = data.count(i)
        napis = i
print(napis, counter)
