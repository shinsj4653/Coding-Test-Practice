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
    start = paper[x][y]
    diff = False

    for i in range(x, x + n):
        for j in range(y, y + n):
            if start != paper[i][j]:
                diff = True
                break
        if diff:
            break

    # for문 안에 return 2 해도 바로 끝남.
    if diff:
        return 2

    else:
        return start


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
