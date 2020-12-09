#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <tuple>
#include <queue>
#include <unordered_set>
#include <stack>
#include <map>

using namespace std;

const int MAX_N = 100000;
const int STEP = 316;

tuple<int, int, int> drogi[MAX_N]; //a, b, c
int misiek_na_drodze_do_miasta[MAX_N + 1];
vector<int> polaczenia[MAX_N + 1];

int rodzic[MAX_N + 1];
int odl_do_pocz[MAX_N + 1];
int pre_order[MAX_N + 1];
int post_order[MAX_N + 1];

unordered_map<int, vector<int>> wybrancy; //id_miasta, [id_miska]<liczba_miskow>
unordered_map<int, int> wybrancy_count;

//O(1) H4CK!!!
//y = v, x = possible_ancestor
//For two given nodes x and y of a tree T, x is an ancestor of y if and only if x occurs before y in the preorder traversal of T and after y in the post-order traversal.
bool is_ancestor(int possible_ancestor, int v)
{
	return pre_order[possible_ancestor] < pre_order[v] && post_order[possible_ancestor] > post_order[v];
}

void ustaw_rodzice()
{
	rodzic[1] = -1;
	queue<int> q;
	q.push(1);
	while (q.size() > 0)
	{
		int v = q.front();
		q.pop();

		for (int i = 0; i < polaczenia[v].size(); i++)
		{
			if (polaczenia[v][i] != rodzic[v])
			{
				rodzic[polaczenia[v][i]] = v;
				q.push(polaczenia[v][i]);
			}
		}
	}
}

void ustaw_pre_order()
{
	stack<int> s;
	s.push(1);
	int last = 0;

	while (s.size() > 0)
	{
		int v = s.top();
		pre_order[v] = last;
		last++;
		s.pop();

		for (int i = 0; i < polaczenia[v].size(); i++)
		{
			if (polaczenia[v][i] != rodzic[v])
			{
				s.push(polaczenia[v][i]);
			}
		}
	}
}

void ustaw_post_order()
{
	stack<int> s1, s2;
	s1.push(1);
	
	while (s1.size() > 0)
	{
		int v = s1.top();
		s1.pop();
		s2.push(v);

		for (int i = polaczenia[v].size() - 1; i >= 0; i--)
		{
			if (polaczenia[v][i] != rodzic[v])
			{
				s1.push(polaczenia[v][i]);
			}
		}
	}

	int last = 0;
	while (!s2.empty())
	{
		int v = s2.top();
		s2.pop();
		post_order[v] = last;
		last++;
	}
}

void ustaw_miski_na_drodze_do_miasta_i_uporzadkuj_drogi()
{
	for (auto& it : drogi)
	{
		if (is_ancestor(get<1>(it), get<0>(it)))
		{
			int a = get<0>(it);
			int b = get<1>(it);
			get<1>(it) = a;
			get<0>(it) = b;
		}
		int c = get<2>(it);
		misiek_na_drodze_do_miasta[get<1>(it)] = c;
	}
}

void ustaw_odl_do_pocz()
{
	queue<int> q;
	q.push(1);
	odl_do_pocz[1] = 0;

	while (q.size() > 0)
	{
		int v = q.front();
		q.pop();

		if (v != 1)
		{
			odl_do_pocz[v] = odl_do_pocz[rodzic[v]] + 1;
		}

		for (size_t i = 0; i < polaczenia[v].size(); i++)
		{
			if (polaczenia[v][i] != rodzic[v])
			{
				q.push(polaczenia[v][i]);
			}
		}
	}
}

vector<int> get_order()
{
	vector<pair<int, int>> sodp; //<city_id, odl_do_pocz>
	for (size_t i = 0; i < MAX_N + 1; i++)
	{
		sodp.push_back(make_pair(i, odl_do_pocz[i]));
	}
	sort(sodp.begin(), sodp.end(), [](const pair<int, int>& lhs, const pair<int, int>& rhs)
		{
			return lhs.second > rhs.second;
		});

	vector<int> order;
	order.reserve(MAX_N + 1);
	for (size_t i = 0; i < MAX_N + 1; i++)
	{
		order.push_back(sodp[i].first);
	}

	return order;
}

bool usuniete[MAX_N + 1];//city_id

void init_wybranca_i_updatnij_usuniete(int x)
{
	for (size_t i = 0; i < STEP; i++)
	{
		x = rodzic[x];
	}

	vector<int> m;
	m.resize(150001);
	wybrancy[x] = m;

	queue<int> q;
	q.push(x);

	while (q.size() > 0)
	{
		int v = q.front();
		q.pop();

		usuniete[v] = true;

		for (size_t i = 0; i < polaczenia[v].size(); i++)
		{
			if (polaczenia[v][i] != rodzic[v] && wybrancy.find(polaczenia[v][i]) == wybrancy.end())
			{
				q.push(polaczenia[v][i]);
			}
		}
	}
}

void wybierz_wybrancow()
{
	vector<int> m;
	m.resize(150001);
	wybrancy[1] = m;

	vector<int> order = get_order(); //[in_order_descending_by_odl_do_pocz]city_id	
	
	int limit = MAX_N / STEP;
	int i = 1;
	while (wybrancy.size() < limit && i < order.size() && odl_do_pocz[order[i]] > STEP)
	{
		if (!usuniete[order[i]])
		{
			init_wybranca_i_updatnij_usuniete(order[i]);
		}
		i++;
	}
}

void ustaw_wybranca_dfs(int v, int wyb, int l_wyb)
{
	if (v == l_wyb)
	{
		return;
	}
	wybrancy[wyb][misiek_na_drodze_do_miasta[v]]++;
	if (wybrancy[wyb][misiek_na_drodze_do_miasta[v]] == 1)
	{
		wybrancy_count[wyb]++;
	}
	ustaw_wybranca_dfs(rodzic[v], wyb, l_wyb);
}

void przypisz_wartosci_wybrancom()
{
	queue<pair<int, int>> q;
	q.push(make_pair(1, 1));

	while (q.size() > 0)
	{
		int v = q.front().first;
		int l_wyb = q.front().second;
		q.pop();

		if (wybrancy.find(v) != wybrancy.end() && v != 1)
		{
			wybrancy[v] = wybrancy[l_wyb];
			wybrancy_count[v] = wybrancy_count[l_wyb];
			ustaw_wybranca_dfs(v, v, l_wyb);
			l_wyb = v;
		}

		for (size_t i = 0; i < polaczenia[v].size(); i++)
		{
			if (polaczenia[v][i] != rodzic[v])
			{
				q.push(make_pair(polaczenia[v][i], l_wyb));
			}
		}
	}
}

int ile_miskow(int x)
{
	unordered_set<int> miski_set;

	while (wybrancy.find(x) == wybrancy.end())
	{
		miski_set.insert(misiek_na_drodze_do_miasta[x]);
		x = rodzic[x];
	}

	int result = wybrancy_count[x];
	for (auto& it : miski_set)
	{
		if (wybrancy[x][it] == 0)
		{
			result++;
		}
	}

	return result;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int n, m, z;
	scanf("%d%d%d", &n, &m, &z);

	for (size_t i = 1; i <= n - 1; i++)
	{
		int a, b, c;
		scanf("%d%d%d", &a, &b, &c);

		drogi[i] = make_tuple(a, b, c);
		polaczenia[a].push_back(b);
		polaczenia[b].push_back(a);
	}

	ustaw_rodzice();	
	ustaw_pre_order();
	ustaw_post_order();
	ustaw_miski_na_drodze_do_miasta_i_uporzadkuj_drogi();
	ustaw_odl_do_pocz();
	wybierz_wybrancow();
	przypisz_wartosci_wybrancom();
	
	for (size_t j = 0; j < z; j++)
	{
		char type;
		scanf("%s", &type);

		if (type == 'Z')
		{
			int x;
			scanf("%d", &x);

			printf("%d\n", ile_miskow(x));
		}
		else //type == 'B'
		{
			int i, c;
			scanf("%d%d", &i, &c);

			int backup = get<2>(drogi[i]);
			get<2>(drogi[i]) = c;
			misiek_na_drodze_do_miasta[get<1>(drogi[i])] = c;

			for (auto& it : wybrancy)
			{
				if ((is_ancestor(get<0>(drogi[i]), it.first) && is_ancestor(get<1>(drogi[i]), it.first)) 
					|| (is_ancestor(get<0>(drogi[i]), it.first) && get<1>(drogi[i]) == it.first) || (is_ancestor(get<1>(drogi[i]), it.first) && get<0>(drogi[i]) == it.first))
				{
					it.second[backup]--;
					if (it.second[backup] == 0)
					{
						wybrancy_count[it.first]--;
					}

					it.second[c]++;
					if (it.second[c] == 1)
					{
						wybrancy_count[it.first]++;
					}
				}
			}
		}
	}
	
	return 0;
}
