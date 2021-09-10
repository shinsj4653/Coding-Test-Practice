import math

# 본인들의 예상 순위 - 자리 순위 -> 정렬활용하여 그 차이를 최대한 없애기!
n = int(input())
rank = []
result = 0

for i in range(n):
    rank.append(int(input()))

rank.sort()

for r in rank:
    result += math.abs(r - (rank.index(r) + 1))

print(result)
