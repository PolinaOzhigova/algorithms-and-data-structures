#include <iostream>
#include <stdlib.h>
#include <time.h>
#define _USE_MATH_DEFINES
#include <cmath>
#include <fstream>
using namespace std;

double random(double min, double max)
{
    return (double)(rand()) / RAND_MAX * (max - min) + max;
}

int main()
{
    int n;
    double number1, number2, number3;
    string name;
    cin >> n >> name;
    name += ".txt";
    ofstream out(name);

    srand(time(0));
    for (int i = 0; i < n; i++)
    {
        number1 = random(-M_PI, M_PI);
        number2 = random(-M_PI, M_PI);
        number3 = random(-M_PI, M_PI);
        out << number1 << " " << number2 << " " << number3 << endl;
    }
    cout << name;

    return 0;
}