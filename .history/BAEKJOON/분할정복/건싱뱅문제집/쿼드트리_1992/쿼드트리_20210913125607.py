n = int(input())
video = []
compressList = []

for i in range(n):
    video.append(input())


def isAllSame(n, x, y):

    countNum = 0

    for i in range(x, x + n):
        for j in range(y, y + n):
            countNum += int(video[i][j])

    # All 0
    if countNum == 0:
        return 0

    # All 1
    elif countNum == n * n:
        return 1

    # Different
    else:
        return -1


# print(video)
def compress(n, x, y):

    num = isAllSame(n, x, y)

    if num == 1:
        compressList.append("1")

    elif num == 0:
        compressList.append("0")

    else:
        compressList.append("(")

        compress(n // 2, x, y)
        compress(n // 2, x, y + n // 2)
        compress(n // 2, x + n // 2, y)
        compress(n // 2, x + n // 2, y + n // 2)

        compressList.append(")")


compress(n, 0, 0)

for c in compressList:
    print(c, end="")
