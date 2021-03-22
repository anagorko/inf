#include <iostream>
#include <string>
#include <vector>

using namespace std;

double f1(double x)
{
	return -1.00000 + 1.80861 * x + 0.00000 * x * x + 0.19139 * x * x * x;
}

double f2(double x)
{
	return 1.14833 - 4.63636 * x + 6.44498 * x * x - 1.95694 * x * x * x;
}

double f3(double x)
{
	return -51.59809 + 74.48325 * x - 33.11483 * x * x + 4.63636 * x * x * x;
}

double f4(double x)
{
	return 224.47368 - 201.58852 * x + 58.90909 * x * x - 5.58852 * x * x * x;
}

double f5(double x)
{
	return -307.12440 + 197.11005 * x - 40.76555 * x * x + 2.71770 * x * x * x;
}

void z1()
{
	cout << "z1: " << endl;
	cout << f2(1.5) << endl;
	cout << endl;
}

void z2()
{
	double max = f1(0);
	double argmax = 0;

	double step = 0.000001;
	for (double x = 0; x < 5; x += step)
	{
		if (x < 1)
		{
			if (f1(x) > max)
			{
				max = f1(x);
				argmax = x;
			}
		}
		else if (x < 2)
		{
			if (f2(x) > max)
			{
				max = f2(x);
				argmax = x;
			}
		}
		else if (x < 3)
		{
			if (f3(x) > max)
			{
				max = f3(x);
				argmax = x;
			}
		}
		else if (x < 4)
		{
			if (f4(x) > max)
			{
				max = f4(x);
				argmax = x;
			}
		}
		else if (x < 5)
		{
			if (f5(x) > max)
			{
				max = f5(x);
				argmax = x;
			}
		}
	}

	cout << "z2: " << endl;
	cout << "x: " << argmax << endl;
	cout << "y: " << max << endl;
	cout << endl;
}

double find_root_f1()
{
	double a = 0;
	double b = 0.9;
	double epsilon = 0.00001;

	//z rysunku wiem, że nie ma miejsca zerowego w a ani b

	while (true)
	{
		double x = (a + b) / 2;
		
		if (abs(f1(x)) < epsilon) return x;

		if (f1(x)*f1(a) > 0) a = x;
		else b = x;
	}
}

double find_root_f3()
{
	double a = 2;
	double b = 2.9;
	double epsilon = 0.00001;

	//z rysunku wiem, że nie ma miejsca zerowego w a ani b

	while (true)
	{
		double x = (a + b) / 2;

		if (abs(f3(x)) < epsilon) return x;

		if (f3(x) * f3(a) > 0) a = x;
		else b = x;
	}
}

double find_root_f4()
{
	double a = 3;
	double b = 3.9;
	double epsilon = 0.00001;

	//z rysunku wiem, że nie ma miejsca zerowego w a ani b

	while (true)
	{
		double x = (a + b) / 2;

		if (abs(f4(x)) < epsilon) return x;

		if (f4(x) * f4(a) > 0) a = x;
		else b = x;
	}
}

double find_root_f5()
{
	double a = 4;
	double b = 4.9;
	double epsilon = 0.00001;

	//z rysunku wiem, że nie ma miejsca zerowego w a ani b

	while (true)
	{
		double x = (a + b) / 2;

		if (abs(f5(x)) < epsilon) return x;

		if (f5(x) * f5(a) > 0) a = x;
		else b = x;
	}
}

void z3()
{
	vector<double> roots;

	//z rysunku widzę, gdzie mniej więcej są miejsca zerowe
	roots.push_back(find_root_f1());
	roots.push_back(find_root_f3());
	roots.push_back(find_root_f4());
	roots.push_back(find_root_f5());

	cout << "z3: " << endl;
	for (size_t i = 0; i < roots.size(); i++)
	{
		cout << roots[i] << endl;
	}
	cout << endl;
}

int main()
{
	z1();
	z2();
	z3();
}
