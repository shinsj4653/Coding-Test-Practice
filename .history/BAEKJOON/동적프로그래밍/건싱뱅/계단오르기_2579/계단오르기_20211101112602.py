n = int(input())
stair = []
score = 0
for i in range(6):
    stair.append(int(input()))

d = [0]
d.append(stair[0])

for i in range(2, n + 1):
    d.append(max(stair[i] + d[i - 2], stair[i] + d[i - 1] + d[i - 3]))
