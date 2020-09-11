# Zajęcia z informatyki 2020-21

## Zajęcia

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
