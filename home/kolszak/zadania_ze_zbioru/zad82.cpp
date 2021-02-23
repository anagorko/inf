#include <iostream>
#include <string>

using namespace std;

int odleglosci_do_rzeki[151];

int liczba_cyfr(int v)
{
	int result = 0;
	while (v > 0)
	{
		result++;
		v /= 10;
	}

	return result;
}

int main()
{
	int px = 0, py = 0;
	int dublony = 0; //+2 dnia 3, 34, 64, 95, 126

	//dzień 85 - 24 grudnia	
	int px_z1;
	int py_z1;

	int dystans = 0;

	int dublony_tortuga = 0;

	int przeciwnicy = 0;

	for (size_t i = 1; i <= 150; i++)
	{
		py += 8;
		px += 11;

		dystans += 19;

		int nowe_dub = liczba_cyfr(py);

		if (i == 3 || i == 34 || i == 64 || i == 95 || i == 126)
		{
			nowe_dub += 2;
		}

		if (nowe_dub >= 4)
		{
			przeciwnicy += nowe_dub;
		}

		dublony += nowe_dub;

		px -= nowe_dub;
		dystans += nowe_dub;

		odleglosci_do_rzeki[i] = abs(px - py);

		if (i == 85)
		{
			px_z1 = px;
			py_z1 = py;
		}

		if (i % 7 == 4)
		{
			dublony_tortuga += dublony / 10;
			dublony -= dublony / 10;
		}
	}

	double avg = 0;
	double sum = 0;
	for (size_t i = 1; i <= 151; i++)
	{
		sum += odleglosci_do_rzeki[i];
	}
	avg = sum / 150;

	cout << "82.1:" << endl;
	cout << "x: " << px_z1 << endl;
	cout << "y: " << py_z1 << endl;
	cout << endl << endl;

	cout << "82.2:" << endl;
	cout << dystans << endl;
	cout << endl << endl;

	cout << "82.3:" << endl;
	cout << dublony_tortuga << endl;
	cout << endl << endl;

	cout << "82.4:" << endl;
	cout << przeciwnicy << endl;
	cout << endl << endl;

	cout << "82.5:" << endl;
	/*cout << "odleglosci od rzeki:" << endl;
	for (size_t i = 1; i <= 150; i++)
	{
		cout << odleglosci_do_rzeki[i] << endl;
	}*/
	cout << "srednia odleglosc od rzeki:" << endl;
	cout << round(avg * 100) / 100 << endl;	
	cout << endl << endl;
}
