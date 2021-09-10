from collections import deque

def solution(board):
    #오, 아래, 왼, 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    N = len(board)
    
    visited = [[-1] * N for _ in range(N)]
    
    Q = deque()
    
    Q.append([0, 0, 0, 0])
    Q.append([0, 0, 0, 1])
    
    visited[0][0] = 0
    
    while Q:
        now_cost, i, j, d = Q.popleft()
        
        #현재 위치에서 네 방향으로의 위치 확인
        #큐랑 for문 활용하여 네 방향체크하며 나아가기.
        
        #힘들게 if, elif 쓰지 말기!
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            # 경계체크
            if ni < 0 or nj < 0 or ni >= N or nj >= N:
                continue
            # 벽체크
            if board[ni][nj] == 1:
                continue
            # 뒤로가기 체크
            if abs(k-d) == 2:
                continue
                
            cost = 100 if k == d else 600
            new_cost = now_cost + cost
            if visited[ni][nj] == -1 or new_cost <= visited[ni][nj]:
                visited[ni][nj] = new_cost
                Q.append([new_cost, ni, nj, k]) 

    return visited[N-1][N-1]