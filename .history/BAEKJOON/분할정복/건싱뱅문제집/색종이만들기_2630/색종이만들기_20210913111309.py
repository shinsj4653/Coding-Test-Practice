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
        if initial == 0:
            whiteAndblue[0] += 1
            return
        else:
            whiteAndblue[1] += 1
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

    whiteAndblue[initial] += n * n
    return


searchPaper(n, x, y, paper, whiteAndblue)

print(white)
print(blue)
