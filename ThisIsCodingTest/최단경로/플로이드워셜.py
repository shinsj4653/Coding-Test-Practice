INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

#자기 자신에서 자기 자신으로 가는 비용 -> 0으로 초기화
for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if a == b :
            graph[a][b] = 0

#각 간선에 대한 정보 입력받아, 그 값으로 초기화
for _ in range(m) :

    a, b, c = map(int, input().split()) #a에서 b로 가는 비용은 c라고 설정
    graph[a][b] = c

for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1) :
    for b in range(1, n + 1) :

        if graph[a][b] == INF :
            print("INFINITY", end = " ")

        else :
            print(graph[a][b], end = " ")

    print()
