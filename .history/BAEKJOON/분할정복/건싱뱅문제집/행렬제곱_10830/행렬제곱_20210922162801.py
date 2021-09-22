n, b = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

for loop in range(b):

    for i in range(n):
        for j in range(n):
            sum = 0
            for num in range(n):
                sum += A[i][j + num] * A[i + num][j]

            A[i][j] = sum
