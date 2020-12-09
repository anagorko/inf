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

void test()
{
    //to_digits_reversed test
    vector<int> d = to_digits_reversed(123549);
    for (size_t i = 0; i < d.size(); i++)
    {
        cout << d[i]; // 945321
    }
    cout << endl << endl;

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
    for (size_t i = 1; i < 1000000; i++)
    {
        if (is_palindrome(to_digits_reversed(i)) && is_palindrome(to_bin_reversed(i)))
        {
            sum += i;
        }
    }
    cout << sum << endl;

    return 0;
}
