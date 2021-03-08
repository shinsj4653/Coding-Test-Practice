#미로탈출 : bfs가 효과적 -> 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문.
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

dx = [1, 0]#최단경로이므로 아래랑 오른쪽으로만 이동
dy = [0, 1]

def bfs(x, y) :

    queue = deque()
    queue.append((x, y))

    while queue :

        x, y = queue.popleft()

        #현재 위치에서 두 방항으로의 위치 확인
        for i in range(2) : 
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue

            if graph[nx][ny] == 0 :
                continue

            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1 #값을 누적하여 더해서 노드에 넣기 -> 거리계산가능.
                queue.append((nx, ny))

    return graph[n - 1][m - 1]
    

print(bfs(0, 0))


        
    
        
