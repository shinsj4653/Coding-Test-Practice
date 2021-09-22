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

    if n == 1:
        whiteAndblue[initial] += 1
        return

    elif n >= 2:
        for i in range(n):
            for j in range(n):
                if initial != paper[i][j]:
                    n //= 2
                    searchPaper(n, x, y, paper, whiteAndblue)
                    searchPaper(n, x, y + n, paper, whiteAndblue)
                    searchPaper(n, x + n, y, paper, whiteAndblue)
                    searchPaper(n, x + n, y + n, paper, whiteAndblue)

                else:
                    whiteAndblue[initial] += n * n
                    return


searchPaper(n, x, y, paper, whiteAndblue)

for num in whiteAndblue:
    print(num)
