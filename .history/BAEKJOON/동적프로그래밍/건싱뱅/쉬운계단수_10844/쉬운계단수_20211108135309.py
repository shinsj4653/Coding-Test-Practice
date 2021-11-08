n = int(input())
d = [1] * 10  # 0 ~ 9


if n == 1:
    print()
else:

    for i in range(2, n + 1):
        d[i] = (2 ** (i - 1)) * 8 + 1

    print(d[n])
