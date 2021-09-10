import heapq
n, l = map(int, input().split())
q = []
result = []

for i in range(n) :
    start, end = map(int, input().split())
    heapq.heappush(q, (start, end))
    
for i in range(1, len(q)) :
    if q[i - 1][0] <= q[i][0] <= q[i - 1][1] : #웅덩이끼리 겹치는 순간..
        