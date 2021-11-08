n = int(input())
d = [0] * 101
d[1] = 9
d[2] = 17

for i in range(1, n + 1):
    if i == 1 or i == 2:
        break
    else:
        d[i] = (2 ** (i - 1)) * 8 + 1 - (2 ** (i - 3))
print(d[n])
