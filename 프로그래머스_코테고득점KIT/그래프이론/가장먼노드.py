# from collections import deque
# import heapq

# def solution(n, edge):
#     global answer
#     answer = 0
    
#     graph = [[] for _ in range(n + 1)]
    
#     visited = [False] * (n + 1)
    
#     for i in edge :
#         i.sort()
#         a, b = i
#         graph[a].append(b)
        
    
#     q = deque([1])
#     visited[1] = True
    
    
    
#     while q :
        
#         node = q.popleft()
#         v = False
        
#         for i in graph[node] :
#             v = True
            
#             if visited[i] == False :
                
#                 q.append(i)
#                 visited[i] = True
            
#         if v == False :
#             answer += 1
#             v = True    

    
#     return answer

# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

#bfs 떠올렸는데..아닌가??
#인터넷 풀이
from collections import deque


def solution(n, edge):
     
    answer = 0
    visited = [False] * (n + 1)
    
    graph = [[] for _ in range(n + 1)]
    
    for e in edge :
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    q = deque()
    q.append(1)
    visited[1] = True
    
    while q :
        answer = len(q)
        #길이 저장해두고 그 만큼 FOR문 돌려서 q안 원소들 뽑아서 다 방문한 상태면 끝까지 왔다는 상태 -> while문 벗어나서 answer 가 자연스레 정답.
        for i in range(answer) :
            
            current = q.popleft()
            
            for c in graph[current] :
                if visited[c] == False :
                    visited[c] = True
                    q.append(c)
        
    
    return answer
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
#너가 BFS 원리를 잘 알고있니를 물어본 문제!!

#또다른 풀이


def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer