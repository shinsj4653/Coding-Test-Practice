da = [0] * 21
db = [0] * 21
dc = [0] * 21

da[0] = 1
db[0] = 1
dc[0] = 1


def w(a, b, c):
    


while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        w(a, b, c)
