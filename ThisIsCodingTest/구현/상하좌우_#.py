#구현 예제 4-1
n = int(input())
x, y = 1, 1
plans = input().split()

#L, R, U, D
dx = [0, 0, -1, 1]#행
dy = [-1, 1, 0, 0]#열

#좌표 더하기 빼기 -> 위로 간다고 +1 이렇게 생각하면 안됨
#위로가면 행의 좌표수가 "감소"함 -> 주의

move_types = ['L', 'R', 'U', 'D']

for plan in plans :

    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue

    x = nx
    y = ny

print(x, y)