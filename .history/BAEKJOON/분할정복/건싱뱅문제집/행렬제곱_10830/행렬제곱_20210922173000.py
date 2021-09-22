# 곱셈 1629번과 유사
n, b = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))


def cal(A, b):

    newA = []
    for i in range(n):
        rowA = []
        for j in range(n):
            sum = 0
            for num in range(n):
                sum += ((A[i][num] % 1000) * (A[num][j] % 1000)) % 1000
            rowA.append(sum % 1000)
        newA.append(rowA)

    A = newA


def multiply(A, b):
    if b == 1:
        return

    else:
        multiply(A, b // 2)
        if b % 2 == 0:
            cal(
                newA,
            )
        else:
            cal(newA, 2 * b + 1)


multiply(A, b)
print(A)
