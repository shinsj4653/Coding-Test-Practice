#include <stdio.h>

void transposeMat(int *A, int m, int n);

int main()
{
    int a[3][4] = {
        {1, 2, 3, 4},
        {3, 0, -2, 4},
        {-1, 1, 0, 3},
    };

    transposeMat((*a)[3], 3, 4);

    return 0;
}
void transposeMat(int *A, int m, int n)
{

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d", *A[i][j]);
        }
        print("\n");
    }
}