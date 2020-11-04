# Zajęcia z informatyki 2020-21

## Zajęcia

## Arkusz kalkulacyjny

### 4 listopada

Na początku proszę uważnie przerobić materiały ze strony [ucze-sie.pl](http://smurf.mimuw.edu.pl/uczesie/?q=arkusz).

### Lista zadań

Dane do zadań można znaleźć w katalogu [dane_do_zadan/](https://github.com/anagorko/inf/tree/master/dane_do_zadan/).

* Liczba PI - [matura maj 2016, zad. 4](https://www.cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_od_2015/MIN-R2_1P-162.pdf)
* Bruker - informator maturalny, [zad. 17](https://www.cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Informatory/2015/Informatyka.pdf)
* Telefony - informator maturalny, [zad. 18](https://www.cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Informatory/2015/Informatyka.pdf)

### Lista funkcji

* `vlookup()`
* `right()` , `left()` 
* `countif()` lub `countifs()` zlicza ilosc elementow pod okreslonymi warunkami. druga funkcja pozwala podawac kilka warunków.
* `and()` , `or()` funkcja koniunkcji oraz alternatywy
* `mod()` funkcja modulo przyjmuje jako argumenty liczbę a i b, zwraca a mod b. 
* `$` , `&` - operator konkatenacji (sklejenia)
* `sum()`
* `if()` 
* `mid()`
* `value()`
* `iferror()`
* `floor()` - zwraca wartość zaokrągloną do dołu, z precyzją (drugi argument) np. `=floor(2,3;3)` zwraca `0`
* `ceiling()` - zaokrąglanie do góry, z precyzją (drugi argument) np. `=ceiling(2,3;2)` zwraca `4`
* `<>` - symbol nierówność w EXCELu, (nie `!=`)
* `month()`, `day()`, `year()` - fukcje zwracają wartość liczbową, przedstawiającą numer miesiaca/dnia/roku, w zależności od podanej wejściowej warotść liczbowej
* `weekday(number,[type])` - funkcja zwraca dzień w określony w drugim argumeńcie sposób:
    * 1 or omitted - Numbers 1 (Sunday) through 7 (Saturday). Behaves like previous versions of Microsoft Excel.
    * 2 - Numbers 1 (Monday) through 7 (Sunday).
    * 3 - Numbers 0 (Monday) through 6 (Sunday).
    * 11 - Numbers 1 (Monday) through 7 (Sunday).
    * 12 - Numbers 1 (Tuesday) through 7 (Monday).
    * 13 - Numbers 1 (Wednesday) through 7 (Tuesday).
    * 14 - Numbers 1 (Thursday) through 7 (Wednesday).
    * 15 - Numbers 1 (Friday) through 7 (Thursday).
    * 16 - Numbers 1 (Saturday) through 7 (Friday).
    * 17 - Numbers 1 (Sunday) through 7 (Saturday).
* `text()`- rozbudowana funkcja, do konwersji różnych wartości w liczby, w tekst: https://support.office.com/en-us/article/TEXT-function-20d5ac4d-7b94-49fd-bb38-93d29371225c

### 28 października

Zadania 65, 67.

### 21 października

Zadanie 1 (Ciągi rekurencyjne) i 64 (Obrazki) ze [zbioru zadań CKE](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/Matura_Zbi%C3%B3r_zada%C5%84_Informatyka.pdf).

[Dane do zadań](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Materialy/Zbiory_zadan/inf-pr-dane.zip).

Do domu: zadanie 58.

### 14 października

Na pierwszej lekcji omówimy zadania z [arkusza I części próbnej matury](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Przykladowe_arkusze/2015/informatka_PR/informatyka_PR_czI_A1.pdf).

Na drugiej lekcji rozwiążecie pierwsze zadanie z [arkusza II części tej matury](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Przykladowe_arkusze/2015/informatka_PR/informatyka_PR_czII_A1.pdf). [Pliki do arkusza](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Przykladowe_arkusze/2015/informatka_PR/dane_czII.zip).

### 9 października

Kontynuujemy implementację kodowania Huffmana. Dotychczasowa implementacja.

```python
def encode(text: str, table: Dict[str, str]) -> str:
    """1 + 2 -> 3"""
    output = []
    for letter in text:
        output.append(table[letter])
    return ''.join(output)


def decode(text: str, tree: Dict) -> str:
    """3 + 4 -> 1"""
    i = iter(text)
    result = []
    t = tree
    while True:
        if isinstance(t, str):
            result.append(t)
            t = tree
        else:
            bit = next(i, None)
            if bit is None:
                break
            elif bit == "0":
                t = t[0]
            elif bit == "1":
                t = t[1]
    return "".join(result)


def code_to_tree(code: Dict) -> dict:
    tree = dict()


    def str_to_tree_rec(value: str, key: str, drzewo: Dict):
        if len(drzewo) is 1:
            drzewo[value[0]] = key

        if drzewo.get(value[0], False) is not None:
            str_to_tree_rec(value[1:], key, drzewo[value[0]])
        else:
            drzewo[value[0]] = {}
            str_to_tree_rec(value[1:], key, drzewo[value[0]])
```

Do zrobienia.

* Komentarze
* Testy
* Dokończenie implementacji `code_to_tree`
* Zaimplementowanie `tree_to_code`
* Zaimplementowanie `generate_tree`
* Wymyślenie sposobu zapisu/odczytu drzewa z kodowaniem
* Projekt i implementacja funkcji `encode_to_file` (potrzebna biblioteka [bitstream](https://pypi.org/project/bitstream/))
* Projekt i implementacja funkcji `decode_from_file` (znów przyda się [bitstream](https://pypi.org/project/bitstream/))

### 2 października

Dzis trudniejszy temat: [kodowanie Huffmana](https://pl.wikipedia.org/wiki/Kodowanie_Huffmana).

Nie dostajecie gotowych sygnatur funkcji (czy klas). 
Na lekcji omówimy działanie algorytmu i spróbujemy wspólnie zaprojektować struktury danych oraz sygnatury funkcji na nich działających.

Do omówienia są operacje:

* Kompresja, gdy mamy *dany* zestaw kodów odpowiadających kodowanym symbolom (przyjmijmy, że tekst zawsze dzielimy na pojedyńcze litery). Czy do kompresji właściwe jest drzewo Huffmana, czy może inna struktura?
* Dekompresja, gdy mamy *dane* drzewo Huffmana.
* Konwersja pomiędzy strukturami z powyższych dwóch punktów.
* Tworzenie drzewa Huffmana dla danego tekstu.


### 30 września

* Przeczytamy wspólnie [rozwiązanie zadania anagramy](text/anagrams.py). Wynik działania programu na [słowniku ponad 100 tysięcy polskich słów](https://ftp.icm.edu.pl/packages/wordlists/polish/):

```
adekr ['darek', 'derka', 'kadre', 'kedra', 'kreda', 'radek', 'redak']
den ['den', 'dne', 'edn', 'end', 'nde', 'ned']
dhq ['dhq', 'dqh', 'hdq', 'hqd', 'qdh', 'qhd']
dot ['dot', 'dto', 'odt', 'otd', 'tdo', 'tod']
efj ['efj', 'ejf', 'fej', 'fje', 'jef', 'jfe']
efq ['efq', 'eqf', 'feq', 'fqe', 'qef', 'qfe']
egl ['egl', 'elg', 'gel', 'gle', 'leg', 'lge']
ehj ['ehj', 'ejh', 'hej', 'hje', 'jeh', 'jhe']
ejs ['ejs', 'esj', 'jes', 'jse', 'sej', 'sje']
aeknr ['ekran', 'karne', 'kerna', 'nerka', 'ranek', 'ranke']
eimn ['emin', 'mein', 'mien', 'mine', 'mnie', 'niem']
epr ['epr', 'erp', 'per', 'pre', 'rep', 'rpe']
eps ['eps', 'esp', 'pes', 'pse', 'sep', 'spe']
est ['est', 'ets', 'set', 'ste', 'tes', 'tse']
fin ['fin', 'fni', 'ifn', 'inf', 'nfi', 'nif']
ghi ['ghi', 'gih', 'hgi', 'hig', 'igh', 'ihg']
gps ['gps', 'gsp', 'pgs', 'psg', 'sgp', 'spg']
hpu ['hpu', 'hup', 'phu', 'puh', 'uhp', 'uph']
ips ['ips', 'isp', 'pis', 'psi', 'sip', 'spi']
ipt ['ipt', 'itp', 'pit', 'pti', 'tip', 'tpi']
aklsu ['kalus', 'klaus', 'kulas', 'lasku', 'lukas', 'luska']
aaklp ['kapal', 'kapla', 'klapa', 'lapka', 'palak', 'palka']
aiklw ['kiwal', 'kwali', 'lawki', 'walki', 'wikla', 'wilka']
alpu ['lapu', 'lupa', 'palu', 'paul', 'pula', 'upal']
lrt ['lrt', 'ltr', 'rlt', 'rtl', 'tlr', 'trl']
ailns ['lsnia', 'silna', 'slain', 'slina', 'snail', 'snila']
mop ['mop', 'mpo', 'omp', 'opm', 'pmo', 'pom']
aoprw ['opraw', 'parow', 'porwa', 'prawo', 'prowa', 'prwoa']
ceiisw ['siwiec', 'swicie', 'swieci', 'wiesci', 'wiesic', 'wiscie', 'wisiec']
```

Warto wspomnieć tu informatyczną zasadę "garbage in garbage out".

* Wyznaczymy ochotnika, który opracuje krótką informację na temat algorytmów [wyszukiwania wzorca w tekście](https://en.wikipedia.org/wiki/String-searching_algorithm).

* Pozostały czas spędzimy na rozwiązaniu [zadania '21. Podzielność'](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Informatory/2015/Informatyka.pdf) ze strony 71 informatora maturalnego. [Pliki z danymi](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Informatory/2015/Informatyka-Dane-i-rozwiazania.zip).

* Dla osób, którym zadanie 21 nie sprawiło problemu, jest zadanie [Don't Get Rooked](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=108&page=show_problem&problem=580). Proszę zwrócić uwagę, że zadanie pochodzi z kategorii [Brute Force::Backtracking](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=108) (znaczenie tych słów wyjaśnię zainteresownym).

### 23 września

* W katalogu [text/](text/) utwórz plik `anagram.py` i zaimplementuj funkcję

```
def is_anagram(a: str, b: str) -> bool
```

zwracającą `True` jedynie jeśli wyrazy `a` i `b` są anagramami.

Następnie napisz program, który znajduje wszystkie grupy anagramów w [słowniku wyrazów angielskich](https://raw.githubusercontent.com/dwyl/english-words/master/words.txt). Znajdź

- grupę najliczniejszą
- grupę (nie jedno-elementową) z największą liczbą liter.

Algorytmy omówimy na zajęciach.

* W katalogu [numeric/](numeric/) w pliku `bisect.py` zaimplementuj funkcję

```
def zero_bisect(f: Callable[[float], float], a: float, b: float, precision: float) -> float
```
znajdującą miejsce zerowe funkcji `f` w przedziale `[a, b]` z dokładnością `precision` (metodą bisekcji). Zakładamy, że znaki `f(a)` i `f(b)` są różne a funkcja `f` jest ciągła.

Wykorzystaj tę funkcję do obliczenia wartości `log_2 3` (logarytmu z 3 o podstawie 2).

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
