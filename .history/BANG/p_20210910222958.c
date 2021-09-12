#include <stdio.h>

void transposeMat(int (&A)[3][4], int m, int n)
{

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            printf("%d", &(&A[i])[j]);
        }
        printf("\n");
    }
}

int main(void)
{
    int a[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};

    transposeMat(a, 3, 4);

    return 0;
}
