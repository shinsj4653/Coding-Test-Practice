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
        elif paper[x][y] == 1:
            return 1
        else:
            return -1
    else:
        for i in range(x, x + n):
            for j in range(y, y + n):
                sum += paper[i][j]

    return sum


def countResult(x, y, n):
    global countZero
    global countOne
    global countMinus

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
        countResult(x, y, n)
        countResult(x + n, y, n)
        countResult(x, y + n, n)
        countResult(x + n, y + n, n)
        countResult(x + 2 * n, y, n)
        countResult(x, y + 2 * n, n)
        countResult(x + 2 * n, y + 2 * n, n)
        countResult(x + n, y + 2 * n, n)
        countResult(x + 2 * n, y + n, n)


countResult(0, 0, n)
print(countMinus)
print(countZero)
print(countOne)
