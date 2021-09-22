# 곱셈 1629번과 유사
n, b = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))


def cal(A):

    newA = []
    for i in range(n):
        rowA = []
        for j in range(n):
            sum = 0
            for num in range(n):
                sum += (A[i][num]) * (A[num][j])
            rowA.append(sum)
        newA.append(rowA)

    return newA


def multiply(A, b):
    if b == 1:
        return 1

    else:
        multiply(A, b // 2)
        if b % 2 == 0:
            A = cal(A)
        else:
            newA = cal(A)
            A = cal(newA)


multiply(A, b)
print(A)
