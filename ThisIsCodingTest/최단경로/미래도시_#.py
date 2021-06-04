INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if a == b :
            graph[a][b] = 0

for i in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    #도로가 이어져 있기만 하면, ab 나 ba나 모두 1임을 인지못함..
    graph[b][a] = 1

x, k = map(int, input().split()) #k를 거쳐서 x번 회사로



for i in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

if graph[1][k] + graph[k][x] >= INF :
    print(-1)

else :
    print(graph[1][k] + graph[k][x])
