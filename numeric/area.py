"""
Zaimplementuj algorytm obliczania pola pod wykresem funkcji pisząc funkcję o sygnaturze

def area(f: Callable[[float], float], a: float, b: float, n: int) -> float:

gdzie f to dana funkcja, a i b to granice całkowania zaś n to liczba przedziałów w rozbiciu [a, b].

Proszę przetestować program i zmianę dokładności wyniku obliczając pole pod wykresem funkcji y = 2sqrt(1 - x^2).

def f(x: float) -> float:
  return 2 * (1 - x * x) ** (1/2)

a = area(f, -1, 1, n)    # interesuje nas zmiana wyniku dla różnych wartości n
"""
