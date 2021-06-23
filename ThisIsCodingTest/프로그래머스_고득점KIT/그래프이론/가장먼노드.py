def dfs(visited, graph, i) :
    
    visited[i] = True
    global answer
    
    a = False
    
    for i in graph[i] :
        
        if visited[i] == False :
            a = True
            dfs(visited, graph, i)
    
    if a == False :
        answer += 1
    

def solution(n, edge):
    global answer
    answer = 0
    
    graph = [[] for _ in range(n + 1)]
    
    visited = [False] * (n + 1)
    
    for i in edge :
        a, b = i
        graph[a].append(b)
    
    
    dfs(visited, graph, 1)
    
    return answer

print()