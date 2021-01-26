//Piotr Trzaskowski Zadanie Szyfr - Meet in the middle optymalna pamięciowo
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<tuple>
#include<string>

using namespace std;

const int MAXN = 40;

int n;
int S;

int a[MAXN];

vector<pair<int, unsigned long long>> half[2];
stack<tuple<int, int, unsigned long long>> Q;

int generateHalf(int half_number)
{
	int begin = (n / 2) * half_number;
	int end = (n - 1) * half_number + (n / 2 - 1) * (half_number - 1) * -1;

	int len = end - begin + 1;
	Q.push(make_tuple(1, 0, 0));
	Q.push(make_tuple(1, a[begin], 1));
	while (!Q.empty())
	{
		int l, d;
		unsigned long long bin;
		tie(l, d, bin) = Q.top();
		Q.pop();
		if (l < len)
		{
			Q.push(make_tuple(l + 1, d, bin * 10));
			Q.push(make_tuple(l + 1, d + a[begin + l], bin * 10 + 1));
		}
		else
			half[half_number].push_back(make_pair(d, bin));
	}
	return len;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];
	cin >> S;

	int len1 = generateHalf(0);
	int len2 = generateHalf(1);

	sort(half[0].begin(), half[0].end());
	sort(half[1].begin(), half[1].end());



	int i = 0;
	int j = half[1].size() - 1;
	bool ok = false;
	while (i < half[0].size() && j >= 0 && !ok)
	{
		if (half[0][i].first + half[1][j].first < S)
			i++;
		else if (half[0][i].first + half[1][j].first > S)
			j--;
		else
			ok = true;
	}

	string bin1 = to_string(half[0][i].second);
	string bin2 = to_string(half[1][j].second);


	while (bin1.length() < len1)
		bin1 = "0" + bin1;
	while (bin2.length() < len2)
		bin2 = "0" + bin2;

	cout << bin1 + bin2 << endl;

	return 0;
}
