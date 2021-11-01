n = int(input())
stair = [0]
score = 0
for i in range(n):
    stair.append(int(input()))

d = [0]
d.append(stair[0])
if n > 1:
    d.append(stair[0] + stair[1])

for i in range(3, n + 1):
    d.append(max(stair[i] + d[i - 2], stair[i] + d[i - 1] + d[i - 3]))

print(d[n])
