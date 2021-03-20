#include<iostream>
#include<fstream>
#include<map>
#include<string>
#include<set>
#include<algorithm>
#include<math.h>

using namespace std;

char filename[] = "dane_wybory.txt";

string komitety[5] = {"K1", "K2", "K3", "K4", "K5"};
string name[20] = {"A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5"};
int tablica_glosow[20][5];
int tablica_glosow_regionalnych[4][5];
int dane_regionalne[4][5];

int tab[2];
int glosy[2];

int dane[20][5];

double wk(int gk, int mk)
{
	return round((gk / (double)(2 * mk + 1))*100)/100;
}

int main()
{
	fstream plik(filename, ios::in);
	if (!plik.good())
	{
		cout << "Error" << endl;
		exit(0);
	}
	int i = 0;
	while (i < 20)
	{
		string n;
		int a, b, c, d, e;
		plik >> n;
		plik >> a; plik >> b; plik >> c; plik >> d; plik >> e;
		dane[i][0] = a; dane[i][1] = b; dane[i][2] = c; dane[i][3] = d; dane[i][4] = e;
		i++;

	}
	//1

	for (int i = 0; i < 20; i++)
	{
		long sum = 0;
		for (int j = 0; j < 5; j++)
		{
			sum += dane[i][j];
		}
		cout << name[i] << "\t" << sum << endl;
	}
	//3
	for (int i = 0; i < 20; i++)
	{
		set<pair<double, int>> suma_pomocnicza;
		for (int j = 0; j < 5; j++)
		{
			suma_pomocnicza.insert({dane[i][j], j});
		}
		int mandaty = 20;
		while (mandaty > 0)
		{
			auto it = suma_pomocnicza.end();
			it--;
			tablica_glosow[i][it->second] ++;
			suma_pomocnicza.insert({wk(dane[i][it->second], tablica_glosow[i][it->second]), it->second});
			suma_pomocnicza.erase(it);
			mandaty--;
		}
	}
	for (int j = 0; j < 5; j++)
	{
		int maxi = 0;
		int bol = 0;
		for (int i = 0; i < 20; i++)
		{
			if (tablica_glosow[i][j] > maxi)
			{
				maxi = tablica_glosow[i][j];
				bol = i;
			}
		}
		cout << komitety[j] << " : " << tablica_glosow[bol][j] << endl;
	}
	//4
	cout << " Standardowy" << endl;
	for (int j = 0; j < 5; j++)
	{
		int sum = 0;
		int bol = 0;
		for (int i = 0; i < 20; i++)
		{
			sum += tablica_glosow[i][j];
		}
		cout << komitety[j] << " : " << sum << endl;
	}
	cout << " Regionany" << endl;
	for (int i = 0; i < 5; i++)
		for (int j = 0; j < 5; j++)
			dane_regionalne[0][j] += dane[i][j];
	for (int i = 5; i < 10; i++)
		for (int j = 0; j < 5; j++)
			dane_regionalne[1][j] += dane[i][j];
	for (int i = 10; i < 15; i++)
		for (int j = 0; j < 5; j++)
			dane_regionalne[2][j] += dane[i][j];
	for (int i = 15; i < 20; i++)
		for (int j = 0; j < 5; j++)
			dane_regionalne[3][j] += dane[i][j];
	for (int i = 0; i < 4; i++)
	{
		set<pair<double, int>> suma_pomocnicza;
		for (int j = 0; j < 5; j++)
		{
			suma_pomocnicza.insert({ dane_regionalne[i][j], j });
		}
		int mandaty = 100;
		while (mandaty > 0)
		{
			auto it = suma_pomocnicza.end();
			it--;
			tablica_glosow_regionalnych[i][it->second] ++;
			suma_pomocnicza.insert({ wk(dane_regionalne[i][it->second], tablica_glosow_regionalnych[i][it->second]), it->second });
			suma_pomocnicza.erase(it);
			mandaty--;
		}
	}
	for (int j = 0; j < 5; j++)
	{
		int sum = 0;
		int bol = 0;
		for (int i = 0; i < 4; i++)
		{
			sum += tablica_glosow_regionalnych[i][j];
		}
		cout << komitety[j] << " : " << sum << endl;
	}
	//5
	int m = 10;
	for (int g = 1; g <= 100000; g++)
	{
		int g2 = 100000 - g;
		tab[1] = g;
		tab[0] = g2;
		glosy[0] = 0;
		glosy[1] = 0;
		set<pair<double, int>> suma_pomocnicza;
		suma_pomocnicza.insert({ g2, 0 });
		suma_pomocnicza.insert({ g, 1 });

		int mandaty = 2*m;
		while (mandaty > 0)
		{
			auto it = suma_pomocnicza.end();
			it--;
			glosy[it->second] ++;
			suma_pomocnicza.insert({wk(tab[it->second], glosy[it->second]), it->second});
			suma_pomocnicza.erase(it);
			mandaty--;
		}
		if (glosy[1] == m)
		{
			cout << g << endl;
			break;
		}
	}
	m = 20;
	for (int g = 1; g <= 100000; g++)
	{
		int g2 = 100000 - g;
		tab[1] = g;
		tab[0] = g2;
		glosy[0] = 0;
		glosy[1] = 0;
		set<pair<double, int>> suma_pomocnicza;
		suma_pomocnicza.insert({ g2, 0 });
		suma_pomocnicza.insert({ g, 1 });

		int mandaty = 2 * m;
		while (mandaty > 0)
		{
			auto it = suma_pomocnicza.end();
			it--;
			glosy[it->second] ++;
			suma_pomocnicza.insert({ wk(tab[it->second], glosy[it->second]), it->second });
			suma_pomocnicza.erase(it);
			mandaty--;
		}
		if (glosy[1] == m)
		{
			cout << g << endl;
			break;
		}
	}
	m = 50;
	for (int g = 1; g <= 100000; g++)
	{
		int g2 = 100000 - g;
		tab[1] = g;
		tab[0] = g2;
		glosy[0] = 0;
		glosy[1] = 0;
		set<pair<double, int>> suma_pomocnicza;
		suma_pomocnicza.insert({ g2, 0 });
		suma_pomocnicza.insert({ g, 1 });

		int mandaty = 2 * m;
		while (mandaty > 0)
		{
			auto it = suma_pomocnicza.end();
			it--;
			glosy[it->second] ++;
			suma_pomocnicza.insert({ wk(tab[it->second], glosy[it->second]), it->second });
			suma_pomocnicza.erase(it);
			mandaty--;
		}
		if (glosy[1] == m)
		{
			cout << g << endl;
			break;
		}
	}
	return 0;
}