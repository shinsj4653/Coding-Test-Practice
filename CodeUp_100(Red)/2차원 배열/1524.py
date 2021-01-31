import sys

mine = []
r_mine = [[0] * 11 for _ in range(11)]


for i in range(9) :
    mine.append(list(map(int, input().split())))

for i in range(9) :
    for j in range(9) :
        r_mine[i + 1][j + 1] = mine[i][j]

r, c = map(int, input().split())


if r_mine[r][c] == 1 :
    print(-1)
    sys.exit()

else :
    count = 0
    count = r_mine[r - 1][c - 1] + r_mine[r - 1][c] + r_mine[r - 1][c + 1] + r_mine[r][c - 1] + r_mine[r][c + 1] + r_mine[r + 1][c - 1] + r_mine[r + 1][c] + r_mine[r + 1][c + 1]   
    print(count)