# import heapq

# def find_parent(x, parent) :
    
#     if parent[x] != x :
#         parent[x] = find_parent(parent[x], parent)
        
#     return parent[x]

# def union_parent(a, b, parent) :
#     a = find_parent(a, parent)
#     b = find_parent(b, parent)
    
#     if a > b :
#         parent[a] = b 
    
#     else :
#         parent[b] = a

# def solution(n, results):
#     answer = 0
    
#     graph = [[] for _ in range(n + 1)]
    
#     indegree = [0] * (n + 1) #진입차수
#     outdegree = [0] * (n + 1) #진출차수
    
#     for r in results :
#         a, b = r #a가 이김! b -> a
#         graph[a].append(b)
#         indegree[b] += 1
#         outdegree[a] += 1
    
#     #순서 확실한 애들 넣은 큐
#     #(순위, 번호) 를 우선순위 큐에다가
#     q = []
    
#     parent = [0] * (n + 1)
#     for i in range(n + 1) :
#         parent[i] = i
        
#     for i in range(1, n + 1) :
#         if indegree[i] + outdegree[i] == n - 1 :
#             answer += 1
#             heapq.heappush(q, (1 + outdegree[i], i))
            
#     while q :
#         current, i = heapq.heappop(q)
        
#         for v in graph[i] :
            
#             if find_parent(i, parent) != find_parent(v, parent) :
#                 union_parent(i, v, parent)  
#                 answer += 1
            
#     #print(q)
            
        
    
    
#     return answer

#신장트리랑 위상정렬 혼합인줄 알았는데..까비
#풀이


def solution(n, results):
    
    answer = 0
    
    wins, loses = {} , {} #wins[key] : key가 이긴 사람들의 집합, loses[key] : key가 이기지 못한 사람들의 집합
    
    for i in range(1, n + 1) :
        wins[i], loses[i] = set(), set()
        
    
    for i in range(1, n + 1) :
        for battle in results :
            if battle[0] == i : #i의 승리
                wins[i].add(battle[1])
                
            if battle[1] == i :
                loses[i].add(battle[0])
                
        #i를 이긴 사람들(loses[i])은 i에게 진 사람에겐 반드시 이긴다
        for winner in loses[i] :
            wins[winner].update(wins[i])
            
        
            
        #i에게 진 사람들은(win[i]) i를 이긴 사람들에게는 반드시 진다
        for loser in wins[i] :
            loses[loser].update(loses[i]) #set()로 여러개 값을 한번에 추가하려할때
        
    cnt = 0
    for i in range(1, n + 1) :
        if len(wins[i]) + len(loses[i]) == n - 1:
            #진입차수, 진출차수 대신, 이기고 지는 거에 대한 사전을 따로 만드는 방법기억하기!
            cnt += 1
    
    answer = cnt
        
    
    
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))