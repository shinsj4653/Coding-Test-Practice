# #음료수 얼려먹기랑 유사

def net_dfs(graph, i, visited) :
    
    visited[i] = True
    
    for i in graph[i] :
        if not visited[i] :

            net_dfs(graph, i, visited)
    
    
#dfs하는 방법 외우기..    
        

def solution(n, computers) :
    
    
    answer = 0
    

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for i in range(n) :
        for j in range(n) :
            
            if computers[i][j] == 1 and i != j:
                graph[i + 1].append(j + 1) #그래프화 시킨다음에 net_dfs실행
    
        
    for i in range(1, n + 1) :
        if visited[i] == False :
            net_dfs(graph, i, visited)
            answer += 1
    
    
    
    return answer