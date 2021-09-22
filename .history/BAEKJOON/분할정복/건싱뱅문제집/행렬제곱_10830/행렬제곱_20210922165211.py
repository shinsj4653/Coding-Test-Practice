from sys import setrecursionlimit

setrecursionlimit(10 ** 6)
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
                    sum += (A[i][num] % 1000) * (A[num][j] % 1000)
                rowA.append(sum % 1000)
            newA.append(rowA)

        if loop == b - 1:
            return newA
        else:
            makeMatrix(newA)


newA = makeMatrix(A)

for loop in range(b):
    newA = makeMatrix(A)
