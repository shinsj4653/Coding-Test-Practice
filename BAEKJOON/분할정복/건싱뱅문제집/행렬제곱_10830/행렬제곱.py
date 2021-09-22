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
            rowA.append(sum % 1000)
        newA.append(rowA)

    return newA


def loop(A, b):
    if b == 1:
        return A

    elif b == 2:
        return cal(A, A)

    else:
        temp = loop(A, b // 2)
        if b % 2 == 0:
            return cal(temp, temp)
        else:
            return cal(cal(temp, temp), A)


A = loop(A, b)
for i in range(n):
    for j in range(n):
        print(A[i][j] % 1000, end=" ")

    print()
