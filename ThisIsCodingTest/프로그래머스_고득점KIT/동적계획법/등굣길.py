def dfs(x, y, road, m, n) : 
    global answer
    
    if x == n - 1 and y == m - 1 :
        answer += 1
        return
    
    
    
    if x + 1 < n : 
        if road[x + 1][y] != 1:
            dfs(x + 1, y, road, m, n)
    
    if y + 1 < m :
        if road[x][y + 1] != 1 :
            dfs(x, y + 1, road, m, n)
        
    else :
        return
        

def solution(m, n, puddles):
    global answer
    
    answer = 0

    
    #m : 열, n : 행
    road = [[0] * m for _ in range(n)]
    
    #1 : 퍼들
    for puddle in puddles :
        col, row = puddle
        road[row - 1][col - 1] = 1
        
    #2 : 도착지점
    #road[n - 1][m - 1] = 2
    
    x = 0
    y = 0
    
    dfs(x, y, road, m, n)
    
    return answer

print(solution(4, 3, [[2, 2]]))

#윗 풀이 시간초과...효율적인 방법 ??

def solution(m, n, puddles):
    
    answers = [[0] * (m + 1) for i in range(n + 1)]
    answers[1][1] = 1
    for i in range(1, n + 1) : #행
        for j in range(1, m + 1) : #열
            if i == 1 and j == 1 :
                continue
            
            if [j, i] in puddles :
                answers[i][j] = 0
                
            else :
                answers[i][j] = answers[i - 1][j] + answers[i][j - 1]
    
    return answer[n][m] % 1000000007

#경로 경우의 수 : 올 수 있는 방향에서 숫자들 더하기!
#못가는 곳은 0으로! 인덱스 오류 피하기 위해서 행, 열 하나씩 추가
# answer[2][3] 으로 오는 방법은 (1, 3) 위, 혹은 (2, 2) 왼쪽 에서 출발해야하는 것.