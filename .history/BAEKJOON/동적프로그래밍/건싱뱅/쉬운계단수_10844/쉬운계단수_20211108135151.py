n = int(input())
d = [0] * 9  # 0 ~ 8
d[1] = 9

if n == 1:
    print(d[n])
else:

    for i in range(2, n + 1):
        d[i] = (2 ** (i - 1)) * 8 + 1

    print(d[n])
