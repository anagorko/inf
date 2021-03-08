x = 0
y = 0
dukaty = 0
odl = []
mile = 0
straty = 0
wojsko = 0
for i in range(1, 151):
    y += 8
    x += 11
    mile += 19
    temp_dukaty = len(str(y))
    if i == 3 or i == 34 or i == 64 or i == 95 or i == 126:
        temp_dukaty += 2

    dukaty += temp_dukaty
    x += -temp_dukaty
    mile += temp_dukaty
    if i == 85:
        print("noc wigilijna: ", x, y)
    if (i - 4) % 7 == 0:
        strata = 0.1*dukaty
        straty += strata
        dukaty = dukaty - strata
    if temp_dukaty > 3:
        wojsko += temp_dukaty
    odl.append(abs(x-y))

print("mile: ", mile)
print("straty: ", straty)
print("wojsko: ", wojsko)
