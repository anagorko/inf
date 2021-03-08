f = open("dane_geny.txt")
dane = []

for i in f:
    dane.append(i.rstrip("\n"))
# print(dane)

gatunki = []
for i in range(500):
    gatunki.append(0)

maximum = 0
for i in dane:
    if len(i) > maximum:
        maximum = len(i)
    gatunki[len(i)-1] += 1
print("liczba gatunkow: ", 500 - gatunki.count(0), "najwiecej: ", max(gatunki))
print("________________69.2______________")


def return_gens(genom):
    result = []
    gen = ""
    pocz_gen = False
    for x in range(len(genom)-1):
        if genom[x] == "A" and genom[x+1] == "A":
            pocz_gen = True
        if genom[x] == "B" and genom[x+1] == "B" and pocz_gen:
            pocz_gen = False
            result.append(gen[2:])
            gen = ""
        if pocz_gen:
            gen = gen + genom[x]
    return result


mutant = False
counter = 0
for i in dane:
    for j in return_gens(i):
        if "BCDDC" in j:
            mutant = True
    if mutant:
        counter += 1
        mutant = False
print(counter)

print("________________69.3______________")
maximum = 0
max_gen = 0
for i in dane:
    if maximum < len(return_gens(i)):
        maximum = len(return_gens(i))
    for j in return_gens(i):
        if len(j) > max_gen:
            max_gen = len(j)
print(maximum, max_gen)
