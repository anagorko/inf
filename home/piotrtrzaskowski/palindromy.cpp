#include<iostream>
#include<string>
#include<vector>

using namespace std;

long long int suma = 0;

const int n = 1000 * 1000;

vector<string> generuj_ciaga(int maxval, int len)
{
	//generuje wszystkie możliwe ciągi z cyframi z przedziału 0 do maxval włącznie o długości len
	vector<string> ciag;
	if (len <= 0)
	{
		ciag.push_back("");
		return ciag;
	}
	vector<string> sciag = generuj_ciaga(maxval, len - 1);
	for (auto a : sciag)
	{
		for (int i = 0; i <= maxval; i++)
		{
			ciag.push_back(a + to_string(i));
		}
	}
	return ciag;
}

int zamien_system_na_dziesietna(string bin, int system)
{
	int dec = 0;
	int dwa = 1;
	for (int i = bin.length()-1; i >=0; i--)
	{
		if (bin[i] != 0)
			dec += (int(bin[i])-int('0')) * dwa;
		dwa *= system;
	}
	return dec;
}

bool jest_palindronem(int dec)
{
	string dec1 = to_string(dec);
	int dl = dec1.length() / 2;
	for (int i = 0; i < dl; i++)
		if (dec1[i] != dec1[dec1.length() - i - 1])
			return false;
	return true;
}

void policz_sume_palindromow(int maxval, int n, int len)
{
	if (len <= 1)
	{
		suma += maxval;
		policz_sume_palindromow(maxval,n, 2);
		return;
	}

	vector<string> ciagi = generuj_ciaga(maxval, (len - 2) / 2);

	for (auto a : ciagi)
	{
		string ra = "";
		for (auto c = a.rbegin(); c != a.rend(); c++)
			ra.push_back(*c);

		if (len % 2 == 1)
		{
			for (int i = 0; i <= maxval; i++)
			{
				string ciag = "1" + a + to_string(i) + ra + "1";
				int dec = zamien_system_na_dziesietna(ciag, maxval+1);
				if (dec > n)
					return;

				if (jest_palindronem(dec))
					suma += dec;

			}
		}
		else
		{
			string ciag = "1" + a + ra + "1";
			int dec = zamien_system_na_dziesietna(ciag, maxval + 1);
			if (dec > n)
				return;
			if (jest_palindronem(dec))
				suma += dec;
		}

	}
	policz_sume_palindromow(maxval, n, len + 1);
}


int main()
{
	policz_sume_palindromow(1, n, 1);
	cout << suma << endl;
	return 0;
}