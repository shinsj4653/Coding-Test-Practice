n = int(input())
d = [0] * 10  # 0 ~ 9

for i in range(1, n + 1):
    d[i] = i * 8 + 1 - 1 * (i - 2)

print(d[n] % 1000000000)
