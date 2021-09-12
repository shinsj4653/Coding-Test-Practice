import heapq

n, l = map(int, input().split())
q = []
result = []

for i in range(n):
    start, end = map(int, input().split())
    heapq.heappush(q, (start, end))

q.sort()

result.append(q[0][1] - q[0][0])

for i in range(1, len(q)):
    if q[i - 1][0] <= q[i][0] <= q[i - 1][1] - 1:  # 웅덩이끼리 겹치는 순간..
        result.append((q[i][1] - q[i][0]) - (q[i - 1][1] - q[i][0]))

    else:  # 안겹치면, 그냥 웅덩이 크기만큼 대입.
        result.append(q[i][1] - q[i][0])

total_puddle = sum(result)

if total_puddle % l == 0:
    print(total_puddle // l)

else:
    print(total_puddle // l + 1)

# 만약, 3번째 웅덩이랑 1번째 웅덩이가 겹칠때는???
# 그래서 생각한게 우선순위 큐 -> 크기 정렬이 되니까!
# 근데 왜 틀렸지..
