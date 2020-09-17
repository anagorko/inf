def iterateFibonacci(n):
    tab = [1, 1]
    while(len(tab)<n):
        tab.append(tab[-2] + tab[-1])
    return tab[-1]

def recurseFibonacci(n):
    if n <= 2:
        return 1
    return recurseFibonacci(n-1) + recurseFibonacci(n - 2)

print(iterateFibonacci(30))
print(recurseFibonacci(30))