n = int(input())
paper = []
countZero = 0
countOne = 0
countMinus = 0

for i in range(n):
    paper.append(list(map(int, input().split())))


def countSum(x, y, n):
    sum = 0
    global paper

    if n == 1:
        if paper[x][y] == 0:
            return 0
    if paper[x][y] == 1:
        return 1
    if paper[x][y] == -1:
        return -1

    for i in range(x, x + n):
        for j in range(y, y + n):
            sum += paper[i][j]

    return sum


def countResult():
    global countZero
    global countOne
    global countMinus
    global n
    x = 0
    y = 0

    num = countSum(x, y, n)

    if num == 0:
        countZero += 1
        return

    elif num == 1:
        countOne += 1
        return

    elif num == -1:
        countMinus += 1
        return

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


countResult()
print(countMinus)
print(countZero)
print(countOne)
