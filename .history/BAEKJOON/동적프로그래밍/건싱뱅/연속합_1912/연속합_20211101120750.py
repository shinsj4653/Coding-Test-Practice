n = int(input())
numlist = list(map(int, input().split()))

d = []
d[0] = numlist[0]

for i in range(1, n):
    d[i] = max(numlist[i] + d[i - 1], numlist[i])

print(max(d))
