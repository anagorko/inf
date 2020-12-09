#include <iostream>
#include <algorithm>

using namespace std;

#define li long long int

const int MAXN = 300000;

int n;
li gabloty[MAXN][3]; //index, typ -> ilość
li sumy_pozostalych_dla_kazdego_typu[3][MAXN]; //typ, index -> suma pozostałych dwóch (S)
li wyniki_do_wybrania_kandydatow[3][MAXN]; //typ, index -> S(a) - min(S(b), S(c))
bool any_of_type[3]; //type

li wynik = 0;

int kandydaci_pozycja[3][3]; //type, order sorted -> index
li kandydaci_wyniki[3][3]; //type, order sorted -> suma pozostałych dwóch
int wybrance[3]; //type -> index

li wez_sume_mniejszych(int i)
{
    li result = 0;

    int counter = 0;
    if (counter < 2 && (gabloty[i][0] < gabloty[i][1] || gabloty[i][0] < gabloty[i][2]))
    {
        result += gabloty[i][0];
        counter++;
    }
    if (counter < 2 && (gabloty[i][1] < gabloty[i][0] || gabloty[i][1] < gabloty[i][2]))
    {
        result += gabloty[i][1];
        counter++;
    }
    if (counter < 2 && (gabloty[i][2] < gabloty[i][0] || gabloty[i][2] < gabloty[i][1]))
    {
        result += gabloty[i][2];
        counter++;
    }
    if (counter < 2 && (gabloty[i][0] == gabloty[i][1] || gabloty[i][0] == gabloty[i][2]))
    {
        result += gabloty[i][0];
        counter++;
    }
    if (counter < 2 && (gabloty[i][1] == gabloty[i][0] || gabloty[i][1] == gabloty[i][2]))
    {
        result += gabloty[i][1];
        counter++;
    }
    if (counter < 2 && (gabloty[i][2] == gabloty[i][0] || gabloty[i][2] == gabloty[i][1]))
    {
        result += gabloty[i][2];
        counter++;
    }

    return result;
}

void read_and_setup()
{
    ios::sync_with_stdio(false);
    cin.tie(0);

    for (size_t i = 0; i < 3; i++)
    {
        any_of_type[i] = false;
    }

    cin >> n;

    for (size_t i = 0; i < n; i++)
    {
        cin >> gabloty[i][0];
        cin >> gabloty[i][1];
        cin >> gabloty[i][2];

        sumy_pozostalych_dla_kazdego_typu[0][i] = gabloty[i][1] + gabloty[i][2];
        sumy_pozostalych_dla_kazdego_typu[1][i] = gabloty[i][0] + gabloty[i][2];
        sumy_pozostalych_dla_kazdego_typu[2][i] = gabloty[i][0] + gabloty[i][1];

        li m = min(sumy_pozostalych_dla_kazdego_typu[0][i], min(sumy_pozostalych_dla_kazdego_typu[1][i], sumy_pozostalych_dla_kazdego_typu[2][i]));
        wyniki_do_wybrania_kandydatow[0][i] = sumy_pozostalych_dla_kazdego_typu[0][i] - m;
        wyniki_do_wybrania_kandydatow[1][i] = sumy_pozostalych_dla_kazdego_typu[1][i] - m;
        wyniki_do_wybrania_kandydatow[2][i] = sumy_pozostalych_dla_kazdego_typu[2][i] - m;

        if (gabloty[i][0] != 0)
        {
            any_of_type[0] = true;
        }
        if (gabloty[i][1] != 0)
        {
            any_of_type[1] = true;
        }
        if (gabloty[i][2] != 0)
        {
            any_of_type[2] = true;
        }
    }
}

void wybierz_kandydatow()
{
    for (size_t i = 0; i < 3; i++)
    {
        for (size_t j = 0; j < 3; j++)
        {
            kandydaci_wyniki[i][j] = -1;
        }
    }

    for (size_t i = 0; i < 3; i++)
    {
        for (size_t j = 0; j < n; j++)
        {
            if (kandydaci_wyniki[i][0] == -1 || kandydaci_wyniki[i][0] > wyniki_do_wybrania_kandydatow[i][j])
            {
                li b_w = kandydaci_wyniki[i][0];
                int b_p = kandydaci_pozycja[i][0];
                kandydaci_wyniki[i][0] = wyniki_do_wybrania_kandydatow[i][j];
                kandydaci_pozycja[i][0] = j;

                li b_w2 = kandydaci_wyniki[i][1];
                int b_p2 = kandydaci_pozycja[i][1];
                kandydaci_wyniki[i][1] = b_w;
                kandydaci_pozycja[i][1] = b_p;

                kandydaci_wyniki[i][2] = b_w2;
                kandydaci_pozycja[i][2] = b_p2;
            }
            else if (kandydaci_wyniki[i][1] == -1 || kandydaci_wyniki[i][1] > wyniki_do_wybrania_kandydatow[i][j])
            {
                li b_w = kandydaci_wyniki[i][1];
                int b_p = kandydaci_pozycja[i][1];
                kandydaci_wyniki[i][1] = wyniki_do_wybrania_kandydatow[i][j];
                kandydaci_pozycja[i][1] = j;

                kandydaci_wyniki[i][2] = b_w;
                kandydaci_pozycja[i][2] = b_p;
            }
            else if (kandydaci_wyniki[i][2] == -1 || kandydaci_wyniki[i][2] > wyniki_do_wybrania_kandydatow[i][j])
            {
                kandydaci_wyniki[i][2] = wyniki_do_wybrania_kandydatow[i][j];
                kandydaci_pozycja[i][2] = j;
            }
        }
    }
}

void wybierz_wybrancow_i_dodaj_do_sumy()
{
    for (size_t i = 0; i < 3; i++)
    {
        wybrance[i] = -1;
    }

    li min_w = -1;
    li min_w_sum = 0;
    for (size_t d = 0; d < 3; d++)
    {
        for (size_t p = 0; p < 3; p++)
        {
            for (size_t r = 0; r < 3; r++)
            {
                li w = 0;
                li sum = 0;
                if (any_of_type[0])
                {
                    w += kandydaci_wyniki[0][d];
                    sum += sumy_pozostalych_dla_kazdego_typu[0][kandydaci_pozycja[0][d]];
                }
                if (any_of_type[1])
                {
                    w += kandydaci_wyniki[1][p];
                    sum += sumy_pozostalych_dla_kazdego_typu[1][kandydaci_pozycja[1][p]];
                }
                if (any_of_type[2])
                {
                    w += kandydaci_wyniki[2][r];
                    sum += sumy_pozostalych_dla_kazdego_typu[2][kandydaci_pozycja[2][r]];
                }
                
                if ((kandydaci_pozycja[0][d] != kandydaci_pozycja[1][p]) && 
                    (kandydaci_pozycja[1][p] != kandydaci_pozycja[2][r]) && 
                    (kandydaci_pozycja[2][r] != kandydaci_pozycja[0][d]) && 
                    (w < min_w || min_w == -1))
                {
                    min_w = w;
                    min_w_sum = sum;
                    if (any_of_type[0]) wybrance[0] = kandydaci_pozycja[0][d];
                    if (any_of_type[1]) wybrance[1] = kandydaci_pozycja[1][p];
                    if (any_of_type[2]) wybrance[2] = kandydaci_pozycja[2][r];
                }
            }
        }
    }
    wynik += min_w_sum;
}

void policz()
{
    for (size_t i = 0; i < n; i++)
    {
        bool cnt = false;
        for (size_t j = 0; j < 3; j++)
        {
            if (wybrance[j] == i)
            {
                cnt = true;
            }
        }
        if (cnt)
        {
            continue;
        }

        wynik += wez_sume_mniejszych(i);
    }
}

int main()
{  
    read_and_setup();
    wybierz_kandydatow();
    wybierz_wybrancow_i_dodaj_do_sumy();
    policz();
    cout << wynik << "\n";
}
