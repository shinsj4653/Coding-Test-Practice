import heapq

n = int(input())
meeting = 0
q = []
result = 1

for i in range(n):
    start, end = map(int, input().split())
    # time = end - start  # 시간이 가장 적은 순서대로 정렬
    heapq.heappush(q, (start, end))

q.sort(key=lambda x: x[1])
bigEnd = q[0][1]

for i in range(1, len(q)):
    if bigEnd <= q[i][0]:
        bigEnd = q[i][1]
        result += 1

print(result)
