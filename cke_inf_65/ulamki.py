import math

with open("dane.txt") as fp: lines = fp.read().splitlines()
splited = []
for i in lines: 
  splited.append(i.split(' '))
floats = []
for i in splited:
  floats.append(round(int(i[0])/int(i[1]), 8))

def find_min(data):
  mini = 12000
  for i in data:
    if mini > i:
      mini = i
  return(mini)


def find_all_min(data, min):
  results = []
  for x, i in enumerate(data):
    if i == min:
      results.append(x)
  return results


def find_min_fraction(data):
  mini = 12000
  pos = -1
  for i in find_all_min(data, find_min(data)):
    if int(splited[i][1]) < mini:
      pos = i
      mini = int(splited[i][1])
  return(splited[i])


def num_of_nieskracalne(data):
  result = 0
  for i in data:
    if math.gcd(int(i[0]), int(i[1])) == 1:
      result +=1
  return(result)


def set_nieskracalne(data):
  result = []
  for i in data:
    gcd = math.gcd(int(i[0]), int(i[1]))
    result.append([int(i[0])/gcd, int(i[1])/gcd])
  return(result)


def suma_licznikow(data):
  result = 0
  for i in data:
    result += i[0]
  return(result)


def set_mianownik(data, mianownik):
  result = []
  for i in data:
    gcd = math.gcd(int(i[0]), mianownik)
    gcd2 = math.gcd(int(i[1]), mianownik)
    result.append([(int(i[0])*mianownik)/gcd, (int(i[1])*mianownik)/gcd2])
  return(result)




print(find_min_fraction(floats))
print(num_of_nieskracalne(splited))
print(suma_licznikow(set_nieskracalne(splited)))
print(suma_licznikow(set_mianownik(splited, 4*9*25*49*13)))
