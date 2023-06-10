#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <fstream>
using namespace std;

int main(void)
{
    double x, y, z, angle;
    string name;
    cin >> name;
    ifstream in(name);

    while (in)
    {
        in >> x >> y >> z;
        angle = 2 * sin(x) * sin(y) + cos(z);
        cout << angle << endl;
    }
    
    return 0;
}