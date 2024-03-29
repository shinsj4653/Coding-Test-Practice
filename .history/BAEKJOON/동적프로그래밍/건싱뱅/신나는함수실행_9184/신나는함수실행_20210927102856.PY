da = [0] * 21
db = [0] * 21
dc = [0] * 21

da[0] = 1
db[0] = 1
dc[0] = 1


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    elif a < b < c:
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)

    else:
        return (
            w(a - 1, b, c)
            + w(a - 1, b - 1, c)
            + w(a - 1, b, c - 1)
            - w(a - 1, b - 1, c - 1)
        )


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        value = w(a, b, c)
        print("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(value))
