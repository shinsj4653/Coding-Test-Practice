import heapq #우선순위 큐를 구현하기 위한 힙 자료구조
import sys
input = sys.stdin.readline()
INF = int(1e9) #10억

#노드, 간선의 개수
n, m = map(int, input().split())
#시작 노드 번호 입력받기
start = int(input())
#그래프 정보 담는 리스트
graph = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m) :
    #모든 간선 정보 입력
    a, b, c = map(int, input().split())

    graph[a].append((b, c))

def dijkstra(start) :
    q = []
    #시작 노드로 가기위한 최단 경로는 0으로 설정하여 큐에삽입
    heapq.heappush(q, (0, start))

    distance[start] = 0 
    while q :#큐가 비어있지 않다면, 
        
        dist, now = heapq.heappop(q)

        if distance[now] < dist :#즉, 이미 최단경로가 정해진, 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now] :
            cost = dist + i[1]
            
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1) :

    if distance[i] == INF :
        print("INFINITY")

    else :
        print(distance[i])




