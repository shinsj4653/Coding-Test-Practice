import heapq

n, l = map(int, input().split())
q = []
result = []

for i in range(n):
    start, end = map(int, input().split())
    heapq.heappush(q, (start, end))

result.append(q[0][1] - q[0][0])

for i in range(1, len(q)):
    if q[i - 1][0] <= q[i][0] <= q[i - 1][1]:  # 웅덩이끼리 겹치는 순간..
        result.append((q[i][1] - q[i][0]) - (q[i - 1][1] - q[i][0]))

    else:  # 안겹치면, 그냥 웅덩이 크기만큼 대입.
        result.append(q[i][1] - q[i][0])

total_puddle = sum(result)

if total_puddle % l == 0:
    print(total_puddle // l)

else:
    print(total_puddle // l + 1)
