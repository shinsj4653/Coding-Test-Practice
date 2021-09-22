n = int(input())
paper = []
countZero = 0
countOne = 0
countMinus = 0

for i in range(n):
    paper.append(list(map(int, input().split())))
x = 0
y = 0


def countSum(x, y, n):
    sum = 0

    if n == 1:
        if paper[x][y] == 0:
            return 0
        elif paper[x][y] == 1:
            return 1
        else:
            return -1
    else:
        for x in range(x, x + n):
            for y in range(y, y + n):
                sum += paper[x][y]

        if sum == 0:
            return 0

        elif sum == n * n:
            return 1

        elif sum == -(n * n):
            return -1

        else:
            n = n // 3
            countSum(x, y, n)
            countSum(x + n, y, n)
            countSum(x, y + n, n)
            countSum(x + n, y + n, n)
            countSum(x + 2 * n, y, n)
            countSum(x, y + 2 * n, n)
            countSum(x + 2 * n, y + 2 * n, n)
            countSum(x + n, y + 2 * n, n)
            countSum(x + 2 * n, y + n, n)


def countResult():
    sum = countSum(x, y, n)

    if sum == 0:
        countZero += 1
        return

    elif num == 1:
        countOne += 1

    elif num == -1:
        countMinus += 1


countResult()
print(countZero)
print(countOne)
print(countMinus)
