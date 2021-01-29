h, w = map(int, input().split())
#w : 가로길이
#h : 세로길이
pan = [[0] * w for _ in range(h)]

n = int(input())
#막대개수
for i in range(n) :
    l, d, x, y = map(int, input().split())
    

    if d == 0 : #가로
        for j in range(l) :
            pan[x - 1][y - 1 + j] = 1

    else : #세로
        for j in range(l) :
            pan[x - 1 + j][y - 1] = 1

for i in range(h) :
    for j in range(w) :
        print(pan[i][j], end = " ")
    print("")
    