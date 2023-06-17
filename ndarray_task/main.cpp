#include "ndarray.h"
#include <iostream>
#include <cstring>
using namespace std;

int main(){
    cout<<"\nInteger Arrays\n";

    NDArray<int> matrix1(3, 2);
    NDArray<int> matrix2(2, 3);
    NDArray<int> matrix3(3, 3);

    matrix1.fill_with_zeros();
    matrix2.fill_with_ones();  
    matrix3.fill_with_rand_numb();

    matrix3.matrix_mult(matrix1, matrix2);
    matrix3.matrix_trans();
    matrix3.division("");
    matrix3.division("0");
    matrix3.division("1");

    matrix2[0][0] = 30;
    matrix2[0][1] += 1;
    matrix2[1][0] /= 2;
    matrix2[1][1] *= 3;
    matrix2[1][2] -= 4;
    matrix2.print_array();

    cout<<"\n\n\nFloat Arrays\n";
    NDArray<float> matrix4(2, 3);
    NDArray<float> matrix5(3, 2);
    NDArray<float> matrix6(2, 2);
    matrix6.fill_with_zeros();
    matrix4.fill_with_ones();  
    matrix4.fill_with_rand_numb();
    
    matrix5.fill_with_rand_numb();
    matrix6.matrix_mult(matrix4, matrix5);
    matrix4.matrix_trans();
    matrix4.division("");
    matrix4.division("0");
    matrix4.division("1");

    matrix5[0][0] = 30;
    matrix5[0][1] += 1;
    matrix5[1][0] /= 2;
    matrix5[1][1] *= 3;
    matrix5[2][1] -= 4.5;
    matrix5.print_array();
    cout<<"\n";
    return 0;
}