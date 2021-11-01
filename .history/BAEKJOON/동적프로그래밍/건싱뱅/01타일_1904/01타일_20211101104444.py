n = int(input())
d = [0] * (n + 1)

# 1 하나 or 0 두 개 붙인
d[1] = 1
d[2] = 2

for i in range(n + 1):
    if i < 3:
        continue

    else:
        d[i] = (d[i - 1] + d[i - 2]) % 15746

print(d[n])
