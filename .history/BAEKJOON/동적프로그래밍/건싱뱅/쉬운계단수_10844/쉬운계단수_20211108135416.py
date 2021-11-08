n = int(input())
d = [1] * 10  # 0 ~ 9


if n == 1:
    print(sum(d) - 1)

else:
    d[9] = 0
    d[0] = 1
    for i in range(2, n + 1):
        for i in range(1, 8):
            d[i] = d[i] * 2

    print(d[n])
