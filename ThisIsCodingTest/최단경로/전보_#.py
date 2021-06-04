import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, c = map(int, input().split())
#n, m 의 범위가 충분히 크기 때문에, 우선순위 큐를 이용하여 다익스트라 알고리즘을 작성해야 한다.

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m) :
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start) :

    q = []
    distance[c] = 0
    heapq.heappush(q, (0, c))

    while q :
        
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist :
            continue

        for i in graph[node] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost ,i[0]))

dijkstra(c)

count = 0
max_time = 0
for i in distance :

    if i == INF or i == 0 :
        continue
    count += 1
    
    if i > max_time :
        max_time = i
    #max_time = max(max_time, i) -> 이런식으로도 사용가능.

print(count, max_time)

    