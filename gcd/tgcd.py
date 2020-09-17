def recurseuklides(a, b):
    if b == 0:
        return a
    return recurseuklides(b,  a % b)

def iterableuklides(a, b):
    while b != 0:
        c = b
        b = a%b
        a = c
    return a

print(recurseuklides(12, 4))
print(iterableuklides(4,12))

print(recurseuklides(13, 7))
print(iterableuklides(7,13))

print(recurseuklides(12, 16))
print(iterableuklides(16,12))