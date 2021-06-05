from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)


cities = []

visited = [False] * (n + 1)

visited[x] = True


def dfs(city) :

    global count

    if k == count :
        cities.append(city)
        count = 0
        return


    for c in graph[city] :

        if visited[c] == False :
            visited[c] = True
            count += 1
            dfs(c)

    return cities

count = 0
ans = dfs(x)

for i in range(len(ans)) :
    print(ans[i])

