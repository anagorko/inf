#include <iostream>
#include <string>
#include <vector>

using namespace std;

float f(float x)
{
	return x * x * x * x / 500 - x * x / 200 - 3.0 / 250;
}

float g(float x)
{
	return -x * x * x / 30 + x / 20 + 1.0 / 6;
}

void z1()
{
	float pole_po_wykrojeniu = 0;

	float step = 8.0 / 10000;
	for (float x = 2 + step; x <= 10; x += step)
	{
		pole_po_wykrojeniu += step * f(x);
		pole_po_wykrojeniu += step * -g(x);
	}

	cout << "z1: ";
	cout << pole_po_wykrojeniu << endl;
	cout << endl;
}

void z2()
{
	float obwod = f(10) - g(10) + 8 * 2;

	float step = 8.0 / 100000;
	for (float x = 2 + step; x <= 10; x += step)
	{
		obwod += sqrt((step * step) + (f(x) - f(x - step)) * (f(x) - f(x - step)));
		obwod += sqrt((step * step) + (g(x) - g(x - step)) * (g(x) - g(x - step)));
	}

	cout << "z2: ";
	cout << ceil(obwod) << endl;
	cout << endl;
}

void z3()
{
	int suma = 0;

	for (float x = 9.75; x >= 2; x -= 0.25)
	{
		if (f(x) - g(x) < 1) break;

		suma += f(x) - g(x);
	}

	cout << "z3: ";
	cout << suma << endl;
	cout << endl;
}

int main()
{
	z1();
	z2();
	z3();
}
