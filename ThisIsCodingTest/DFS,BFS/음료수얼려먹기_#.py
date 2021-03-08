n, m = map(int, input().split())
#n : 행
#m : 가로

graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

def dfs(x, y) :

    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    
    if graph[x][y] == 0 : #방문 안한경우

        graph[x][y] = 1#재귀돌리면서 옆에 있는 노드들을 모두 방문처리하게 함으로써 다음 좌표로 32라인 들어갈때 또 세지 않도록하기
        #dfs 활용

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True#방문 안한경우 한 번 진입하면 True를 반환하게 됨. 반환후엔 방문한 노드 또 방문시엔 다 25라인 또는 12라인으로 False처리되어 흘려보냄 
    return False



result = 0
for i in range(n) :
    for j in range(m) :

        if dfs(i, j) == True :
            result += 1
print(result)
    
    

    