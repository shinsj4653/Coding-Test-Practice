#너비우선탐색
#동작원리 : 큐, 구현 방법 : 큐 자료구조 이용
from collections import deque

def bfs(graph, start, visited) :

    queue = deque([start])

    visited[start] = True

    while queue : #큐가 빌때까지 반복

        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True #연결된 노드 모두 큐에 삽입 & 방문처리

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4 ,5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
