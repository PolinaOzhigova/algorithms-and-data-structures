#include <iostream>
#include <map>
#include <chrono>
#include <cmath>
using namespace std;

int main()
{
    map<int, int> test;
    int c;
    for (int i = 0; i <= 7; i++)
    {
        test.clear();
        c = ceil(pow(10, i));
        auto start = chrono::steady_clock::now();
        for (int j = 1; j < c; j++)
        {
            test[j] = j;
        }
        auto end = chrono::steady_clock::now();
        cout << chrono::duration_cast<chrono::milliseconds>(end - start).count()
        << " " << sizeof(int) * 2 * c <<" ";
    }
}