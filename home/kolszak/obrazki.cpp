#include <iostream>
#include <string>
#include <vector>
#include <tuple>

using namespace std;

bool d[200][20][20];
bool parz_x[200][20];
bool parz_y[200][20];

int black_count(int id)
{
	int black = 0;
	for (size_t x = 0; x < 20; x++)
	{
		for (size_t y = 0; y < 20; y++)
		{
			if (d[id][x][y])
			{
				black++;
			}
		}
	}
	return black;
}

bool is_recursive(int id)
{
	for (size_t x = 0; x < 10; x++)
	{
		for (size_t y = 0; y < 10; y++)
		{
			if (!(d[id][x][y] == d[id][x + 10][y] && d[id][x][y] == d[id][x + 10][y + 10] && d[id][x][y] == d[id][x][y + 10]))
			{
				return false;
			}
		}
	}
	return true;
}

pair<int, int> get_state(int id) //0->poprawny 1->naprawialny 2->nienaprawialny
{
	int* cx = new int[20];	
	int* cy = new int[20];
	for (size_t i = 0; i < 20; i++)
	{
		cx[i] = 0;
		cy[i] = 0;
	}

	for (size_t x = 0; x < 20; x++)
	{
		for (size_t y = 0; y < 20; y++)
		{
			cx[x] += d[id][x][y];
			cy[y] += d[id][x][y];
		}
	}

	bool correct = true;
	bool fixable = true;
	int fx = 0;
	int fy = 0;
	for (size_t i = 0; i < 20; i++)
	{
		if (correct)
		{
			correct = (cx[i] % 2) == parz_x[id][i] && (cy[i] % 2) == parz_y[id][i];
		}

		if ((cx[i] % 2) != parz_x[id][i])
		{
			fx++;
			if (fx > 1)
			{
				fixable = false;
			}
		}

		if ((cy[i] % 2) != parz_y[id][i])
		{
			fy++;
			if (fy > 1)
			{
				fixable = false;
			}
		}
	}

	if (correct)
	{
		return make_pair(0, fx + fy);
	}
	else if (fixable)
	{
		return make_pair(1, fx + fy);
	}
	return make_pair(2, fx + fy);
}

pair<int, int> how_to_fix(int id)
{
	pair<int, int> result;

	int* cx = new int[20];
	int* cy = new int[20];
	for (size_t i = 0; i < 20; i++)
	{
		cx[i] = 0;
		cy[i] = 0;
	}

	for (size_t x = 0; x < 20; x++)
	{
		for (size_t y = 0; y < 20; y++)
		{
			cx[x] += d[id][x][y];
			cy[y] += d[id][x][y];
		}
	}	

	int fx = -1;
	int fy = -1;
	for (size_t i = 0; i < 20; i++)
	{
		if ((cx[i] % 2) != parz_x[id][i])
		{
			fx = i;
		}

		if ((cy[i] % 2) != parz_y[id][i])
		{
			fy = i;
		}
	}
	if (fx != -1 && fy != -1)
	{
		result = make_pair(fx, fy);
	}
	else if (fx != -1)
	{
		result = make_pair(fx, 20);
	}
	else if (fy != -1)
	{
		result = make_pair(20, fy);
	}

	return result;
}

int main()
{
	for (size_t i = 0; i < 200; i++)
	{		
		for (size_t x = 0; x < 20; x++)
		{
			string input;
			cin >> input;
			for (size_t y = 0; y < 20; y++)
			{			
				d[i][x][y] = input[y] - '0';
			}
			parz_x[i][x] = input[20] - '0';
		}
		string input2;
		cin >> input2;
		for (size_t y = 0; y < 20; y++)
		{
			parz_y[i][y] = input2[y] - '0';
		}
	}

	int reverse_count = 0;
	int recursive_count = 0;
	int* states_count = new int[3];
	for (size_t i = 0; i < 3; i++)
	{
		states_count[i] = 0;
	}

	vector<tuple<int, int, int>> htf_list;
	int black_max = 0;
	int errors_max = 0;
	int first_recursive_id = -1;
	for (int i = 0; i < 200; i++)
	{
		int bc = black_count(i);
		reverse_count += bc > 200;
		if (bc > black_max)
		{
			black_max = bc;
		}

		bool recursive = is_recursive(i);
		recursive_count += recursive;
		if (first_recursive_id == -1 && recursive)
		{
			first_recursive_id = i;
		}

		pair<int, int> state = get_state(i);
		states_count[state.first]++;
		if (state.first == 1)
		{
			htf_list.push_back(make_tuple(i, how_to_fix(i).first, how_to_fix(i).second));
		}
		if (state.second > errors_max)
		{
			errors_max = state.second;
		}
	}
	cout << "reverse_count: " << reverse_count << endl;
	cout << "black_max: " << black_max << endl; 
	cout << endl;
	cout << "recursive_count: " << recursive_count << endl;
	cout << "first: " << first_recursive_id << " //nie chce mi sie wiec samo id" << endl;
	cout << endl;
	cout << "correct: " << states_count[0] << endl;
	cout << "fixable: " << states_count[1] << endl;
	cout << "unfixable: " << states_count[2] << endl;
	cout << "errors_max: " << errors_max << endl;
	cout << endl;
	cout << "fixes: " << endl;
	for (size_t i = 0; i < htf_list.size(); i++)
	{
		cout << "id: " << get<0>(htf_list[i]) << " x: " << get<1>(htf_list[i]) << " y: " << get<2>(htf_list[i]) << endl;
	}


	return 0;
}
