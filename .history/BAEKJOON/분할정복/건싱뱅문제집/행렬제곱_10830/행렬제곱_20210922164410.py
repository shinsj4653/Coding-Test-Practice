n, b = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

newA = []
for i in range(n):
    rowA = []
    for j in range(n):
        sum = 0
        for num in range(n):
            sum += A[i][i + num] * A[i + num][j]
        rowA.append(sum)
    newA.append(rowA)

print(A)
