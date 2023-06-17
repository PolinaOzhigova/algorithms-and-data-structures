#include <iostream>
#include <ctime>
#include <random>
#include <typeinfo>
#include <iomanip>
#include <time.h> 

using namespace std;

template <typename T>
class NDArray
{
public:
    int x, y;
    T **arr;

    ~NDArray()
    {
        for (int i = 0; i < x; i++)
        {
            delete[] arr[i];
        }
        delete[] arr;
    }

    NDArray(int a, int b)
    {
        x = a;
        y = b;
        arr = new T *[x];
        for (int i = 0; i < x; i++)
        {
            arr[i] = new T[y];
        }
    }

    void fill_with_zeros()
    {
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                arr[i][j] = 0;
            }
        }
        print_array();
        cout << "fill_with_zeros" << endl;
    }

    void fill_with_ones()
    {
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                arr[i][j] = 1;
            }
        }
        print_array();
        cout << "fill_with_ones" << endl;
    }

    void fill_with_rand_numb()
    {
        srand(time(0));
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                arr[i][j] = 0 + ((rand() % (int)pow(10, 2)) / pow(10, 2)) * (10 - 0);
            }
        }
        print_array();
        cout << "fill_with_random_numbers" << endl;
    }

    T *operator[](const int &i)
    {
        return arr[i];
    }

    NDArray<T> &operator=(T &num)
    {
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                arr[i][j] = num;
            }
        }
        return *this;
    }

    NDArray<T> &operator+=(T &num)
    {
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                arr[i][j] += num;
            }
        }
        return *this;
    }

    NDArray<T> &operator-=(T &num)
    {
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                arr[i][j] -= num;
            }
        }
        return *this;
    }

    NDArray<T> &operator/=(T &num)
    {
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                arr[i][j] /= num;
            }
        }
        return *this;
    }

    NDArray<T> &operator*=(T &num)
    {
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                arr[i][j] *= num;
            }
        }
        return *this;
    }

    void print_array()
    {
        for (int i = 0; i < x; i++)
        {
            cout << "\n";
            for (int j = 0; j < y; j++)
            {
                cout << arr[i][j] << "\t";
            }
        }
        cout << "\n";
    }

    void matrix_mult(NDArray<T> &A, NDArray<T> &B)
    {
        if (A.y != B.x)
        {
            cout << endl
                 << "These matrices cannot be multiplied" << endl;
        }
        else
        {
            if (x != A.x or y != B.y)
            {
                cout << endl
                     << "Incorrect dimension of the matrix" << endl;
            }
            else if (x == A.x and y == B.y)
            {
                for (int i = 0; i < A.x; i++)
                {
                    for (int j = 0; j < B.y; j++)
                    {
                        for (int k = 0; k < A.y; k++)
                        {
                            this->arr[i][j] += A[i][k] * B[k][j];
                        }
                    }
                }
                print_array();
                cout << "matrix_multiplication" << endl;
            }
        }
    }

    NDArray<T> matrix_trans()
    {
        NDArray<T> copy(y, x);
        for (int i = 0; i < x; i++)
        {
            for (int j = 0; j < y; j++)
            {
                copy[j][i] = arr[i][j];
            }
        }
        return copy;
    }

    void division(string numb)
    {

        if (numb == "0")
        {
            NDArray<T> mas(1, y);
            T sum = 0;
            for (int i = 0; i < y; i++)
            {
                sum = 0;
                for (int j = 0; j < x; j++)
                {
                    sum = sum + arr[j][i];
                }
                mas[0][i] = sum / x;
            }
            mas.print_array();
            cout << "division by columns" << endl;
        }

        if (numb == "1")
        {
            NDArray<T> mas(1, x);
            T sum = 0;
            for (int i = 0; i < x; i++)
            {
                sum = 0;
                for (int j = 0; j < y; j++)
                {
                    sum = sum + arr[i][j];
                }
                mas[0][i] = sum / y;
            }
            mas.print_array();
            cout << "division by lines" << endl;
        }

        if (numb == "")
        {
            NDArray<T> mas(1, 1);
            T sum = 0;
            for (int i = 0; i < x; i++)
            {
                for (int j = 0; j < y; j++)
                {
                    sum = sum + arr[i][j];
                }
            }
            mas[0][0] = sum / (x * y);
            mas.print_array();
            cout << "division of the entire array" << endl;
        }
    }
};