n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

# print(paper)
x = 0  # 가로
y = 0  # 세로

whiteAndblue = [0, 0]


def searchPaper(n, x, y, paper, whiteAndblue):
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
                    n //= 2
                    searchPaper(n, x, y, paper, whiteAndblue)
                    searchPaper(n, x, y + n, paper, whiteAndblue)
                    searchPaper(n, x + n, y, paper, whiteAndblue)
                    searchPaper(n, x + n, y + n, paper, whiteAndblue)

                    break

    if white == n * n or blue == n * n:
        whiteAndblue[initial] += 1
        return


searchPaper(n, x, y, paper, whiteAndblue)

for num in whiteAndblue:
    print(num)
