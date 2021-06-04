from collections import deque
import copy

#노드의 개수
v = int(input())

indegree = [0] * (v + 1)

graph = [[] for i in range(v + 1)]

time = [0] * (v + 1)

for i in range(1, v + 1) :
    data = list(map(int, input().split()))
    time[i] = data[0]#첫번째 수는 시간 정보를 담고 있음.
    for x in data[1:-1] :#인덱스 1부터 인덱스 -1, 즉 끝자리 직전까지.
        indegree[i] += 1
        graph[x].append(i)#i랑 x 변수 활용

def topology_sort() :
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v + 1) :
        if indegree[i] == 0 :
            q.append(i)

    while q :

        now = q.popleft()

        for i in graph[now] : #i랑 now 변수활용
            result[i] = max(result[i], result[now] + time[i])#max 원리 이해하도록
            indegree[i] -= 1

            if indegree[i] == 0 :
                q.append(i)

    for i in range(1, v + 1) :
        print(result[i])

topology_sort()