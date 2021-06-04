import heapq
import sys

input = sys.stdin.readline #readline() 이거 아님.
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)] #각 노드에 대한 그래프 정보이므로, 행은 n + 1개
array = [INF] * (n + 1)
h = []

for i in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

heapq.heappush(h, (0, start))

def dijkstra(start) :

    array[start] = 0

    while h :

        length, node = heapq.heappop(h) #heappop() 함수안에 힙 있어야함.

        if length > array[node] :#이미 처리된 노드면 무시
            continue

        for i in graph[node] : #i[0] : 인접노드, i[1] : 간선
            cost = length + i[1] #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우

            if cost < array[i[0]] : #cost가 작을때만 array갱신 & 우선순위 큐에 대입
                array[i[0]] = cost
                heapq.heappush(h, (cost, i[0])) #우선순위 큐 안에 넣을때는 cost, i[0] 순으로
                #최단거리를 기준으로 우선순위 큐안에서 정렬해야하기 때문.

dijkstra(start)

for i in range(1, n + 1) :
    if array[i] == INF :
        print("IMPOSSIBLE")

    else :
        print(array[i])


