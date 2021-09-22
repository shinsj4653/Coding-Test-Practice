n, b = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))


def makeMatrix(A):
    for loop in range(b):
        newA = []
        for i in range(n):
            rowA = []
            for j in range(n):
                sum = 0
                for num in range(n):
                    sum += A[i][num] * A[num][j]
                rowA.append(sum)
            newA.append(rowA)


makeMatrix(A)
print(A)
