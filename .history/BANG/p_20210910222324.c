#include <stdio.h>

void transposeMat(int *A, int m, int n)
{

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d", *(*(A[i])[j]));
        }
        printf("\n");
    }
}

int main()
{
    int a1[4] = {1, 2, 3, 4};
    int a2[4] = {11, 12, 13, 14};
    int a3[4] = {21, 22, 23, 24};

    int *a[3] = {a1, a2, a3};

    transposeMat(&a, 3, 4);

    return 0;
}
