from sys import setrecursionlimit

setrecursionlimit(10 ** 6)
n, b = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

loop = 0
while loop < b:
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
        for i in range(n):
            for j in range(n):
                print(newA[i][j], end=" ")
            print()

        break

    else:
        loop += 1
        A = newA
