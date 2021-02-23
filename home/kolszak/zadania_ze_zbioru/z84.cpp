#include <iostream>
#include <string>
#include <fstream>

using namespace std;

const char path[] = "C:\\Users\\IChri\\Downloads\\inf-pr-dane\\dane\\84\\lpg.txt";

int rok = 2014;
int miesiac[366];
int dzien[366];

int km[366];

float lpg_przed_podroza[366];
float lpg_po_podrozy[366];

void z4()
{
	float koszt_zlpg = 1600;
	float koszt_bezlpg = 0;

	float pb95 = 45; // spalanie = 9l / 100km
	float lpg = 30; // spalanie = 6l / 100km

	//bez lpg:
	for (size_t i = 1; i <= 365; i++)
	{
		float spalone_pb95 = 6.0 * km[i] / 100;
		koszt_bezlpg += round(spalone_pb95 * 4.99 * 100) / 100;
	}

	pb95 = 45;
	lpg = 30;

	//z lpg:
	for (size_t i = 1; i <= 365; i++)
	{
		float spalone_pb95 = 0;
		float spalone_lpg = 0;

		if (lpg > 15)
		{
			spalone_lpg = round(9.0 * km[i]) / 100;
			koszt_zlpg += round(spalone_lpg * 2.29 * 100) / 100;
		}
		else
		{
			spalone_lpg = round(0.5 * 9.0 * km[i]) / 100;
			koszt_zlpg += round(spalone_lpg * 2.29 * 100) / 100;

			spalone_pb95 = round(0.5 * 6.0 * km[i]) / 100;
			koszt_zlpg += round(spalone_pb95 * 4.99 * 100) / 100;
		}

		pb95 -= spalone_pb95;
		lpg -= spalone_lpg;

		if (i % 7 == 2) // czwartek
		{
			if (pb95 < 40)
			{
				pb95 = 45;
			}
		}

		if (lpg < 5)
		{
			lpg = 30;
		}
	}
	
	cout << "8.4: " << endl;
	cout << "koszt z lpg: " << koszt_zlpg << endl;
	cout << "koszt bez lpg: " << koszt_bezlpg << endl;
	cout << endl << endl;
}

int main()
{
	fstream plik;
	plik.open(path, ios::in);

	string input;
	plik >> input;
	plik >> input;

	int counter = 2;
	while (plik >> input)
	{
		if (counter % 2 == 0)
		{
			miesiac[counter / 2] = (int)(input[5] - '0') * 10 + (int)(input[6] - '0');
			dzien[counter / 2] = (int)(input[8] - '0') * 10 + (int)(input[9] - '0');
		}
		else
		{
			km[counter / 2] = 0;
			for (int i = input.size() - 1; i >= 0; i--)
			{
				km[counter / 2] += (int)(input[i] - '0') * pow(10, input.size() - 1 - i);
			}
		}

		counter++;
	}

	int dni_lpg_only = 0;

	int tankowania_pb95 = 0;
	int tankowania_lpg = 0;

	float pb95 = 45; // spalanie = 6l / 100km
	float lpg = 30; // spalanie = 9l / 100km

	int dzien_odp_z2 = 0;

	for (size_t i = 1; i <= 365; i++)
	{
		if (dzien_odp_z2 == 0 && lpg < 5.25) dzien_odp_z2 = i;
		lpg_przed_podroza[i] = lpg;

		float spalone_pb95 = 0, spalone_lpg = 0;

		if (lpg > 15)
		{
			spalone_lpg = round(9.0 * km[i]) / 100;
			dni_lpg_only++;
		}
		else
		{
			spalone_lpg = round(0.5 * 9.0 * km[i]) / 100;
			spalone_pb95 = round(0.5 * 6.0 * km[i]) / 100;
		}

		pb95 -= spalone_pb95;
		lpg -= spalone_lpg;

		lpg_po_podrozy[i] = lpg;

		if (i % 7 == 2) // czwartek
		{
			if (pb95 < 40)
			{
				pb95 = 45;
				tankowania_pb95++;
			}
		}
		
		if (lpg < 5)
		{
			lpg = 30;
			tankowania_lpg++;
		}
	}

	/*for (size_t i = 1; i <= 365; i++)
	{
		cout << lpg_po_podrozy[i] << endl;
	}*/

	cout << "84.1: " << endl;
	cout << "tankowania pb95: " << tankowania_pb95 << endl;
	cout << "tankowania lpg: " << tankowania_lpg << endl;
	cout << "liczba dni w ktore Binarny uzywal tylko lpg: " << dni_lpg_only << endl;
	cout << endl << endl;

	cout << "84.2: " << endl;
	cout << rok << "-" << miesiac[dzien_odp_z2] << "-" << dzien[dzien_odp_z2] << endl;
	cout << endl << endl;

	z4();
}
