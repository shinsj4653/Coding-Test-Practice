from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

n = int(input())
test = []
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(n):
    test.append(int(input()))


for num in test:
    sum = 0
    for i in range(1, num):
        sum += d[i]
