# Zajęcia z informatyki 2020-21

## Zajęcia

### 18 września

* W katalogu [sorting/](sorting/) utwórz plik `bucket.py` i zaimplementuj algorytm sortowania kubełkowego pisząc funkcję o sygnaturze
```
def bucket_sort(numbers: List[int], lowest: int, highest: int) -> List[int]:
```
gdzie `lowest` jest najmniejszą wartością w liście a `highest` największą. Nie zapomnij o *unit testach* i porównaj czas działania z czasem działania sortowania bąbelkowego i przez scalanie (wynik porównania pokaż za pomocą wykresu).

* W katalogu [numeric/](numeric/) w pliku `area.py` zaimplementuj algorytm obliczania pola pod wykresem funkcji pisząc funkcję o sygnaturze
```
def area(f: Callable[[float], float], a: float, b: float, n: int) -> float:
```
gdzie `f` to dana funkcja, `a` i `b` to granice całkowania zaś `n` to liczba przedziałów w rozbiciu `[a, b]`.

Proszę przetestować program i zmianę dokładności wyniku obliczając pole pod wykresem funkcji `y = 2sqrt(1 - x^2)`.
```
def f(x: float) -> float:
  return 2 * (1 - x * x) ** (1/2)

a = area(f, -1, 1, n)    # interesuje nas zmiana wyniku dla różnych wartości n
```

* W katalogu [numeric/](numeric/) w pliku `monte.py` zaimplementuj algorytm obliczania wartości liczby pi metodą Monte Carlo omówioną na lekcji.
```
def pi(n: int) -> float:
```
gdzie `n` to liczba prób.

### 16 września

* W katalogu [sorting/](sorting/): napisz implementacje sortowania bąbelkowego, przez wybór i przez scalanie. 
Do każdego napisz testy **i przetestuj czas wykonania**. Wzór jak testować znajdziesz w rozwiązaniu zadania [fibonacci/](fibonacci).

* W katalogu [maxmin/](maxmin/) pokazana jest "naiwna" i "zoptymalizowana" wersja algorytmu znajdującego maksimum i minimum w ciągu wraz z benchmarkiem.

### 11 września

* W katalogu [fibonacci/](fibonacci/): napisz funkcje obliczające n-ty wyraz ciągu 
Fibonacciego na dwa sposoby: iteracyjnie i rekurencyjnie. Napisz testy poprawności i 
porównaj wydajność obu implementacji. 
* W katalogu [gcd](gcd/): napisz funkcje obliczające największy wspólny dzielnik 
liczb a i b na dwa sposoby: iteracyjnie i rekurencyjnie. Napisz testy poprawności.
* W katalogu [number_representation](number_representation/): napisz funkcje konwertujące
liczby na reprezentację binarną, szesnastkową, dziesiętną i z powrotem. Napisz 
testy poprawności.
* W katalogu [primality](primality/): napisz funkcje sprawdzające, czy dana liczba jest pierwsza
  lub doskonała. Napisz testy poprawności.
* W katalogu [greedy_change](greedy_change/): zaimplementuj funkcję 'wydającą resztę' metodą
  zachłanną. Napisz testy poprawności.
  
## Algorytmy

###  Algorytmy na liczbach całkowitych
* [reprezentacja liczb w dowolnym systemie pozycyjnym, w tym
w dwójkowym i szesnastkowym](number_representation/),
* [sprawdzanie, czy liczba jest liczbą pierwszą, doskonałą](primality/),
* [rozkładanie liczby na czynniki pierwsze](divisors/),
* [iteracyjna i rekurencyjna realizacja algorytmu Euklidesa](gcd/),
* [iteracyjne i rekurencyjne obliczanie wartości liczb Fibonacciego](fibonacci/),
* [wydawanie reszty metodą zachłanną](greedy_change/),

### Algorytmy wyszukiwania i porządkowania (sortowania)
* jednoczesne znajdowanie największego i najmniejszego ele-
mentu w zbio rze: algo rytm naiwny i optymalny,
* algorytmy sortowania ciągu liczb: bąbelkowy, przez wybór,
przez wsta wianie linio we lub binarne, przez scalanie, szybki,
kubełkowy,

### Algorytmy numeryczne

* obliczanie wartości pierwiastka kwadratowego,
* obliczanie wartości wielomianu za pomocą schematu Hornera,
* zastosowania schematu Hornera: reprezentacja liczb w różnych syste mach liczbo wych, szybkie podnoszenie do potęgi,
* wyznaczanie miejsc zerowych funkcji metodą połowienia,
* obliczanie pola obszarów zamkniętych,

### Algorytmy na tekstach

* sprawdzanie, czy dany ciąg znaków tworzy palindrom, anagram,
* porządkowanie alfabetyczne,
* wyszukiwanie wzorca w tekście,
* obliczanie wartości wyrażenia podanego w postaci odwrotnej
notacji polskiej,
 
### Algorytmy kompresji i szyfrowania
* kody znaków o zmiennej długości, np. alfabet Morse’a, kod Huffmana,
* szyfr Cezara,
* szyfr przestawieniowy,
* szyfr z kluczem jawnym (RSA),
* wykorzystanie algorytmów szyfrowania, np. w podpisie
elektronicznym,

### Algorytmy badające własności geometryczne
* sprawdzanie warunku trójkąta,
* badanie położenia punktów względem prostej,
* badanie przynależności punktu do odcinka,
* przecinanie się odcinków,
* przynależność punktu do obszaru,
* konstrukcje rekurencyjne: drzewo binarne, dywan Sierpińskiego, płatek Kocha.

## Konfiguracja

Środowisko wirtualne (jednorazowa inicjalizacja)
```
python3 -m venv ~/envs/inf
```

Aktywowanie środowiska
```
source ~/envs/inf/bin/activate
```

Deaktywacja
```
deactivate
```

Upgrade `pip`-a (jednorazowo)
```
python3 -m pip install --upgrade pip
```

Instalacja modułów (jednorazowo)
```
python3 -m pip install pylint
```
