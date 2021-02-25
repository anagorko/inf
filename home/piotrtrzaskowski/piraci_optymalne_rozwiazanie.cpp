#include <boost/date_time/gregorian/gregorian.hpp>
#include <iostream>
#include<string>
#include<math.h>
#include<vector>

using namespace std;

vector<int> odleglosci;

void proceed(int days = 150)
{
    using namespace boost::gregorian;
    date firstDay(1902, 10, 1);
    date wigilia(1902, 12, 24);
    int rzedna = 0;
    int odcieta = 0;
    int suma_mil_przesznietych_na_polnoc = 0;
    int zlote_dublony = 0;
    int liczba_mil = 0;
    int zostawione_dublony = 0;
    int przeciwnicy = 0;
    float odlegloscccc = 0;
    while (days > 0)
    {
        rzedna += 8;
        liczba_mil += 8;
        suma_mil_przesznietych_na_polnoc += 8;
        odcieta += 11;
        liczba_mil += 11;
        int wlasnie_zebralem = to_string(suma_mil_przesznietych_na_polnoc).length();
        if (firstDay.day() == 3)
            wlasnie_zebralem += 2;
        if (wlasnie_zebralem >= 4)
        {
            przeciwnicy += wlasnie_zebralem;
        }
        zlote_dublony += wlasnie_zebralem;
        odcieta -= wlasnie_zebralem;
        liczba_mil += wlasnie_zebralem;
        if (firstDay.day_of_week() == Saturday)
        {
            zostawione_dublony += floor((float)zlote_dublony * 0.1);
            zlote_dublony -= floor((float)zlote_dublony * 0.1);
        }
        if (firstDay == wigilia)
        {
            cout << "Piraci spedza w wigillie noc : " << " rzedna: " << rzedna << " odcieta: " << odcieta << endl;
        }
        odlegloscccc += abs(rzedna - odcieta);
        odleglosci.push_back(abs(rzedna - odcieta));
        firstDay += boost::gregorian::days(1);
        days--;
    }
    cout << "Piraci przejda lacznie: " << liczba_mil << " mil " << endl;
    cout << "Piraci zostawia na Tortudze: " << zostawione_dublony << " zlotych dublonow" << endl;
    cout << "Piraci beda musieli sie zmierzyc z : " << przeciwnicy << " przeciwnikami" << endl;
    cout << "Srednia odleglosc obozu wieczornego piratow od rzeki: " << round((odlegloscccc / 150) * 100) / 100 << endl;
    for (auto a : odleglosci)
    {
        while (a > 0)
        {
            cout << "-";
            a--;
        }
        cout << endl;
    }
    cout << zlote_dublony << endl;
    cout << rzedna << " " << odcieta << endl;
    cout << firstDay << endl;

}

int main() {

    proceed();


    return 0;
}