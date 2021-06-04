from collections import deque

v, e = map(int, input().split())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e) :
    a, b = map(int, input().split())
    graph[a].append(b) #정점 A에서 B로 이동가능

    indegree[b] += 1

#위상 정렬함수
def topology_sort() :
    result = [] #알고리즘 수행 결과를 담을 리스트
    q = deque() #큐 기능을 위한 deque 라이브러리 사용
    
    for i in range(1, v + 1) :
        if indegree[i] == 0 :
            q.append(i)

    while q :
        
        now = q.popleft()
        result.append(now)

        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now] :
            indegree[i] -= 1
            #새롭게 진입 차수가 0이 되는 노드를 큐에 삽입.
            if indegree[i] == 0 :
                q.append(i)

    for i in result :
        print(i, end = " ")

topology_sort()