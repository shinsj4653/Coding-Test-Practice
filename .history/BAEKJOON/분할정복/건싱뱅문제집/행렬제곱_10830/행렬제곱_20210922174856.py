# 곱셈 1629번과 유사
n, b = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))


def cal(A1, A2):

    newA = []
    for i in range(n):
        rowA = []
        for j in range(n):
            sum = 0
            for num in range(n):
                sum += (A1[i][num]) * (A2[num][j])
            rowA.append(sum)
        newA.append(rowA)

    return newA


def multiply(A, b):
    if b == 1:
        return A

    elif b == 2:
        return cal(A, A)

    else:
        if b % 2 == 0:
            return cal(multiply(A, b // 2), multiply(A, b // 2))
        else:
            return cal(cal(multiply(A, b // 2), multiply(A, b // 2)), multiply(A, 1))


multiply(A, b)
print(A)
