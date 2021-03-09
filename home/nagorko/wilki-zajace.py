a = 0.02
b = 0.0005
c = 0.05
z = 100
w = 30

populacja_zajecy = [100]
populacja_wilkow = [30]
for i in range(12*40):
    z = z + a*z - b*z*w
    w = w + b*z*w - c*w
    populacja_zajecy.append(z)
    populacja_wilkow.append(w)

print("____________83.1___________")
print(populacja_zajecy[60], populacja_wilkow[60])
print("____________83.2___________")
for i in range(len(populacja_zajecy)-1):
    if populacja_zajecy[i] > populacja_zajecy[i+1]:
        print("zajace: ", i)
        break

for i in range(len(populacja_wilkow)-1):
    if populacja_wilkow[i] > populacja_wilkow[i+1]:
        print("wilki: ", i)
        break

# print(populacja_wilkow)
print("____________83.4___________")
print(min(populacja_zajecy), max(populacja_zajecy))
print(min(populacja_wilkow), max(populacja_wilkow))
