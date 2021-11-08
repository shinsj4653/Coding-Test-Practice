n = int(input())
d = [0] * (n + 1)

for i in range(1, n + 1):
    d[i] = i * 8 + 1

print(d[n] % 1000000000)
