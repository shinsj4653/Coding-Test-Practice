# 곱셈 1629번과 유사
n, b = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))


def cal(A, b):
    loop = 1
    while loop <= b:
        newA = []
        for i in range(n):
            rowA = []
            for j in range(n):
                sum = 0
                for num in range(n):
                    sum += ((A[i][num] % 1000) * (A[num][j] % 1000)) % 1000
                rowA.append(sum % 1000)
            newA.append(rowA)

        if loop == b:
            return newA
            break

        else:
            loop += 1
            A = newA


def multiply(A, b):
    if b == 1:
        return cal(A, 1)

    else:
        newA = multiply(A, b // 2)
        if b % 2 == 0:
            return cal(newA, 1)
        else:
            return cal(newA, 2)


multiply(A, b)
