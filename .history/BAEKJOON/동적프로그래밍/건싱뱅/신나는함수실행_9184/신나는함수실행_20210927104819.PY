d = [[[0] * 21 for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                d[i][j][k] = 1
            else:
                d[i][j][k] = 0


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        if d[a][b][c] != 0:
            return d[a][b][c]
        else:
            d[a][b][c] = w(20, 20, 20)
            return d[a][b][c]

    elif a < b < c:

        if d[a][b][c] != 0:
            return d[a][b][c]

        else:

            d[a][b][c - 1] = w(a, b, c - 1)
            d[a][b - 1][c - 1] = w(a, b - 1, c - 1)
            d[a][b - 1][c] = w(a, b - 1, c)
        return d[a][b][c - 1] + d[a][b - 1][c - 1] + d[a][b - 1][c]

    else:

        if d[a][b][c] != 0:
            return d[a][b][c]

        else:

            d[a - 1][b][c] = w(a - 1, b, c)
            d[a - 1][b - 1][c] = w(a - 1, b - 1, c)
            d[a - 1][b][c - 1] = w(a - 1, b, c - 1)
            d[a - 1][b - 1][c - 1] = w(a - 1, b - 1, c - 1)

            return (
                d[a - 1][b][c]
                + d[a - 1][b - 1][c]
                + d[a - 1][b][c - 1]
                - d[a - 1][b - 1][c - 1]
            )


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        value = w(a, b, c)
        print("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(value))
