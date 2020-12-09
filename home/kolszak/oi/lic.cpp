#include <iostream>
#include <set>
#include <string>

using namespace std;

const int MAXN = 100000;

int W[MAXN];
int Z[MAXN];
int S[MAXN + 1];

int n, z;

set<int> ciagi_dziewiatek_poczatki;
int ciagi_dziewiatek_konce[MAXN];

bool incremented[MAXN + 1];

void setup()
{
    cin >> n;
    cin >> z;

    string w, z;
    cin >> w;
    cin >> z;

    int dziewiatki_start = -1;
    for (size_t i = 1; i <= n - 1; i++)
    {
        W[i] = int(w[n - 1 - i]) - int('0');
        Z[i] = int(z[n - 1 - i]) - int('0');
        S[i] = (W[i] + Z[i]) % 10;

        if ((W[i] + Z[i]) / 10 == 1)
        {
            incremented[i + 1] = true;
        }
        else
        {
            incremented[i + 1] = false;
        }

        if (dziewiatki_start == -1)
        {
            if (S[i] == 9)
            {
                dziewiatki_start = i;
            }
        }
        else if (S[i] != 9)
        {
            ciagi_dziewiatek_poczatki.insert(dziewiatki_start);
            ciagi_dziewiatek_konce[dziewiatki_start] = i - 1;
            dziewiatki_start = -1;
        }
    }
    if (S[n - 1] == 9)
    {
        ciagi_dziewiatek_poczatki.insert(dziewiatki_start);
        ciagi_dziewiatek_konce[dziewiatki_start] = n - 1;
        dziewiatki_start = -1;
    }
    S[n] = 0;
}

set<int>::iterator get_closest_lower_or_equal(int a)
{
    auto it = ciagi_dziewiatek_poczatki.upper_bound(a);

    if (it != ciagi_dziewiatek_poczatki.begin())
    {
        return --it;
    }

    return it;
}

bool any_lower_or_equal(int a)
{
    auto it = ciagi_dziewiatek_poczatki.upper_bound(a);
    return it != ciagi_dziewiatek_poczatki.begin() && ciagi_dziewiatek_poczatki.size() > 0;
}

set<int>::iterator get_closest_greater(int a)
{
    return ciagi_dziewiatek_poczatki.upper_bound(a);
}

void aktualizuj_ciagi_dziewiatek(int i, int old)
{
    auto c_l = get_closest_lower_or_equal(i);
    auto c_g = get_closest_greater(i);

    // v -> nieznane
    // : -> kraniec
    // x -> cos innego niz 9
    // 9 -> 9

    if (old != S[i])
    {
        if (i == 1 && i == n - 1) // : v :
        {
            if (old == 9) // : 9 : -> : x :
            {
                ciagi_dziewiatek_poczatki.erase(i);
            }
            else if (S[i] == 9) // : x : -> : 9 :
            {
                ciagi_dziewiatek_poczatki.insert(i);
                ciagi_dziewiatek_konce[i] = i;
            }
        }
        else if (i == n - 1) // v v :
        {
            if (S[i - 1] == 9) // 9 v :
            {
                if (old == 9) // 9 9 : -> 9 x :
                {
                    ciagi_dziewiatek_konce[*c_l] = i - 1;
                }
                else if (S[i] == 9) // 9 x : -> 9 9 :
                {
                    ciagi_dziewiatek_konce[*c_l] = i;
                }
            }
            else // x v :
            {
                if (old == 9) // x 9 : -> x x :
                {
                    ciagi_dziewiatek_poczatki.erase(i);
                }
                else if (S[i] == 9) // x x : -> x 9 :
                {
                    ciagi_dziewiatek_poczatki.insert(i);
                    ciagi_dziewiatek_konce[i] = i;
                }
            }
        }
        else if (i == 1) // : v v
        {
            if (S[i + 1] == 9) // : v 9
            {
                if (old == 9) // : 9 9 -> : x 9
                {
                    ciagi_dziewiatek_poczatki.insert(i + 1);
                    ciagi_dziewiatek_konce[i + 1] = ciagi_dziewiatek_konce[i];
                    ciagi_dziewiatek_poczatki.erase(i);
                }
                else if (S[i] == 9) // : x 9 -> : 9 9
                {
                    ciagi_dziewiatek_poczatki.insert(i);
                    ciagi_dziewiatek_konce[i] = ciagi_dziewiatek_konce[i + 1];
                    ciagi_dziewiatek_poczatki.erase(i + 1);
                }
            }
            else // : v x
            {
                if (old == 9) // : 9 x -> : x x
                {
                    ciagi_dziewiatek_poczatki.erase(i);
                }
                else if (S[i] == 9) // : x x -> : 9 x
                {
                    ciagi_dziewiatek_poczatki.insert(i);
                    ciagi_dziewiatek_konce[i] = i;
                }
            }
        }
        else // v v v
        {
            if (S[i - 1] == 9 && S[i + 1] == 9) // 9 v 9
            {
                if (old == 9) // 9 9 9 -> 9 x 9
                {
                    int stary_koniec = ciagi_dziewiatek_konce[*c_l];
                    ciagi_dziewiatek_konce[*c_l] = i - 1;
                    ciagi_dziewiatek_poczatki.insert(i + 1);
                    ciagi_dziewiatek_konce[i + 1] = stary_koniec;
                }
                else if (S[i] == 9) // 9 x 9 -> 9 9 9
                {
                    ciagi_dziewiatek_konce[*c_l] = ciagi_dziewiatek_konce[i + 1];
                    ciagi_dziewiatek_poczatki.erase(i + 1);
                }
            }
            else if (S[i - 1] == 9) // 9 v x
            {
                if (old == 9) // 9 9 x -> 9 x x
                {
                    ciagi_dziewiatek_konce[*c_l] = i - 1;
                }
                else if (S[i] == 9) // 9 x x -> 9 9 x
                {
                    ciagi_dziewiatek_konce[*c_l] = i;
                }
            }
            else if (S[i + 1] == 9) // x v 9
            {
                if (old == 9) // x 9 9 -> x x 9
                {
                    ciagi_dziewiatek_poczatki.insert(i + 1);
                    ciagi_dziewiatek_konce[i + 1] = ciagi_dziewiatek_konce[i];
                    ciagi_dziewiatek_poczatki.erase(i);
                }
                else if (S[i] == 9) // x x 9 -> x 9 9
                {
                    ciagi_dziewiatek_poczatki.insert(i);
                    ciagi_dziewiatek_konce[i] = ciagi_dziewiatek_konce[i + 1];
                    ciagi_dziewiatek_poczatki.erase(i + 1);
                }
            }
            else // x v x
            {
                if (old == 9) // x 9 x -> x x x
                {
                    ciagi_dziewiatek_poczatki.erase(i);
                }
                else if (S[i] == 9) // x x x -> x 9 x
                {
                    ciagi_dziewiatek_poczatki.insert(i);
                    ciagi_dziewiatek_konce[i] = i;
                }
            }
        }
    }
}

void wykonaj_zapytania()
{
    for (size_t j = 0; j < z; j++)
    {
        char typ;
        cin >> typ;

        if (typ == 'W')
        {
            int i, c;
            cin >> i;
            cin >> c;

            int old = S[i];

            W[i] = c;
            S[i] = (W[i] + Z[i]) % 10;

            if ((W[i] + Z[i]) / 10 == 1)
            {
                incremented[i + 1] = true;
            }
            else
            {
                incremented[i + 1] = false;
            }

            aktualizuj_ciagi_dziewiatek(i, old);
        }
        else if (typ == 'Z')
        {
            int i, c;
            cin >> i;
            cin >> c;

            int old = S[i];

            Z[i] = c;
            S[i] = (W[i] + Z[i]) % 10;

            if ((W[i] + Z[i]) / 10 == 1)
            {
                incremented[i + 1] = true;
            }
            else
            {
                incremented[i + 1] = false;
            }

            aktualizuj_ciagi_dziewiatek(i, old);
        }
        else //typ == S
        {
            int i;
            cin >> i;

            if (incremented[i])
            {
                cout << (S[i] + 1) % 10 << "\n";
                continue;
            }

            auto c_l = get_closest_lower_or_equal(i);
            if (any_lower_or_equal(i) && incremented[*c_l])
            {
                if (S[i - 1] == 9 || S[i] == 9)
                {
                    cout << (S[i] + 1) % 10 << "\n";
                    continue;
                }
            }

            cout << S[i] << "\n";
        }
    }
}

int main()
{
    setup();
    wykonaj_zapytania();
}
