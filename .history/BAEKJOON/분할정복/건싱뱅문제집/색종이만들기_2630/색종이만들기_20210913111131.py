n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

# print(paper)
x = 0  # 가로
y = 0  # 세로

global white
white = 0
global blue
blue = 0


def searchPaper(n, x, y, paper, white, blue):
    initial = paper[x][y]

    if n == 1:
        if initial == 0:
            white += 1
            return
        else:
            blue += 1
            return

    elif n >= 2:
        for i in range(n):
            for j in range(n):
                if initial != paper[i][j]:
                    n //= 2
                    searchPaper(n, x, y, paper, white, blue)
                    searchPaper(n, x, y + n, paper, white, blue)
                    searchPaper(n, x + n, y, paper, white, blue)
                    searchPaper(n, x + n, y + n, paper, white, blue)

    if initial == 0:
        white += n * n
        return

    else:
        blue += n * n
        return


searchPaper(n, x, y, paper, white, blue)

print(white)
print(blue)
