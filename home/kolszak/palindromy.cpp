#include <iostream>
#include <vector>

using namespace std;

vector<int> to_digits_reversed(int number)
{
    vector<int> result;

    int digits_count = 7;
    for (size_t i = 1000000; i >= 1; i /= 10)
    {
        if (number / i > 0)
        {
            break;
        }

        digits_count--;
    }
    
    for (size_t i = 0; i < digits_count; i++)
    {
        result.push_back(number % 10);

        number /= 10;
    }

    return result;
}

int digits_to_num_reversed(vector<int> digits)
{
    int result = 0;
    int c = 1;

    for (size_t i = 0; i < digits.size(); i++)
    {
        result += digits[i] * c;

        c *= 10;
    }

    return result;
}

vector<int> to_bin_reversed(int dec)
{
    vector<int> result;

    while (dec > 0)
    {
        result.push_back(dec % 2);
        dec /= 2;
    }

    return result;
}

bool is_palindrome(vector<int> v)
{
    for (size_t i = 0; i < v.size() / 2; i++)
    {
        if (v[i] != v[v.size() - 1 - i])
        {
            return false;
        }
    }

    return true;
}

vector<vector<int>> generate_palindroms_in_range_from_one_to_milion_in_decimal_system()
{
    vector<vector<int>> result;

    for (size_t i = 0; i <= 9; i++)
    {
        for (size_t j = 0; j <= 9; j++)
        {
            for (size_t k = 0; k <= 9; k++)
            {
                result.push_back(vector<int>());
                if (i != 0)
                {
                    result[result.size() - 1].push_back(i);
                }               
                if (i != 0 || j != 0)
                {
                    result[result.size() - 1].push_back(j);
                }
                if (i != 0 || j != 0 || k != 0)
                {
                    result[result.size() - 1].push_back(k);
                }
                if (i != 0 || j != 0 || k != 0)
                {
                    result[result.size() - 1].push_back(k);
                }
                if (i != 0 || j != 0)
                {
                    result[result.size() - 1].push_back(j);
                }
                if (i != 0)
                {
                    result[result.size() - 1].push_back(i);
                }

                result.push_back(vector<int>());
                if (i != 0)
                {
                    result[result.size() - 1].push_back(i);
                }
                if (i != 0 || j != 0)
                {
                    result[result.size() - 1].push_back(j);
                }
                if (i != 0 || j != 0 || k != 0)
                {
                    result[result.size() - 1].push_back(k);
                }
                if (i != 0 || j != 0)
                {
                    result[result.size() - 1].push_back(j);
                }
                if (i != 0)
                {
                    result[result.size() - 1].push_back(i);
                }
            }
        }
    }

    return result;
}

void test()
{
    //to_digits_reversed test
    vector<int> d = to_digits_reversed(123549);
    for (size_t i = 0; i < d.size(); i++)
    {
        cout << d[i]; // 945321
    }
    cout << endl << endl;

    cout << digits_to_num_reversed(d) << endl << endl; // 123549

    //to_bin_reversed test
    d = to_bin_reversed(35);
    for (size_t i = 0; i < d.size(); i++)
    {
        cout << d[i]; // 110001
    }
    cout << endl << endl;

    //is_palindrome test
    d = to_digits_reversed(123321);
    cout << is_palindrome(d) << endl; // 1
    d = to_digits_reversed(123322);
    cout << is_palindrome(d) << endl; // 0
}

int main()
{
    int sum = 0;
    vector<vector<int>> dec_palindroms = generate_palindroms_in_range_from_one_to_milion_in_decimal_system();
    for (auto it : dec_palindroms)
    {
        if (is_palindrome(to_bin_reversed(digits_to_num_reversed(it))))
        {
            sum += digits_to_num_reversed(it);
        }
    }
    cout << sum << endl;
    
    return 0;
}
