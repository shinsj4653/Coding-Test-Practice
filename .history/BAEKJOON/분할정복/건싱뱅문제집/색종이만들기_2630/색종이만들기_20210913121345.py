n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

# print(paper)
x = 0  # 가로
y = 0  # 세로

whiteAndblue = [0, 0]


def searchPaper(n, x, y):

    cycleStop = False
    initial = paper[x][y]
    white = 0
    blue = 0

    if n == 1:
        whiteAndblue[initial] += 1
        return

    elif n >= 2:
        for i in range(x, x + n):
            for j in range(y, y + n):

                if paper[i][j] == 1:
                    blue += 1
                else:
                    white += 1

                if initial != paper[i][j]:
                    cycleStop = True
                    n //= 2
                    searchPaper(n, x, y)
                    searchPaper(n, x, y + n)
                    searchPaper(n, x + n, y)
                    searchPaper(n, x + n, y + n)

                    break

            if cycleStop == True:
                break

    if n > 1 and (white == n * n or blue == n * n):
        whiteAndblue[initial] += 1
        return


searchPaper(n, x, y)

for num in whiteAndblue:
    print(num)
