#벽 또는 자기 자신 : 1 , 빈칸 : 0, 사과 : 2

n = int(input())
snake = [[0] * (n + 2) for _ in range(n + 2)]

#벽 제작
for i in range(n + 2) :

    for j in range(n + 2) :
        if i == 0 or i == n + 1 :
            snake[i][j] = 1
        
        else :
            snake[i][0] = 1
            snake[i][n + 1] = 1



#사과넣기
k = int(input())

for i in range(k) :
    x, y = map(int, input().split())
    snake[x][y] = 2
 
move_list = []
#방향 좌표
l = int(input())
for i in range(l) :
    x, c = input().split() #x : 시간, c : 방향
    move_list.append((x, c))

#뱀 현재좌표
x = 1 #행
y = 1 #열
snake[x][y] = 1
direct = 'r'
pos = [(-1, 0), (1, 0), (0, -1), (0, 1)] #위0, 아래1, 왼2, 오3
time = 0
meet_one = False

for i in move_list :
    
    if meet_one == True :
        break
    #i[0] : 시간, i[1] : 방향
    l_time = i[0]
    l_time = int(l_time)
    l_time -= time

    while l_time > 0 :

        if direct == 'r' :
            
            x += pos[3][0]
            y += pos[3][1]

            if snake[x][y] == 1 : #벽 또는 자기자신
                meet_one = True
                break
                
            elif snake[x][y] == 2 : #사과
                snake[x][y] = 1

            else : #벽, 자기자신 도 아니고 사과도 아닐때
                snake[x][y] = 1
                snake[(x - pos[3][0])][(y - pos[3][1])] = 0

            l_time -= 1
            time += 1

        elif direct == 'l' :

            x += pos[2][0]
            y += pos[2][1]

            if snake[x][y] == 1 : #벽 또는 자기자신
                meet_one = True
                break
                
            elif snake[x][y] == 2 : #사과
                snake[x][y] = 1

            else : #벽, 자기자신 도 아니고 사과도 아닐때
                snake[x][y] = 1
                snake[(x - pos[2][0])][(y - pos[2][1])] = 0

            l_time -= 1
            time += 1
        
        elif direct == 'u' :

            x += pos[0][0]
            y += pos[0][1]

            if snake[x][y] == 1 : #벽 또는 자기자신
                meet_one = True
                break
                
            elif snake[x][y] == 2 : #사과
                snake[x][y] = 1

            else : #벽, 자기자신 도 아니고 사과도 아닐때
                snake[x][y] = 1
                snake[(x - pos[0][0])][(y - pos[0][1])] = 0

            l_time -= 1
            time += 1

        elif direct == 'd' :

            x += pos[1][0]
            y += pos[1][1]

            if snake[x][y] == 1 : #벽 또는 자기자신
                meet_one = True
                break
                
            elif snake[x][y] == 2 : #사과
                snake[x][y] = 1

            else : #벽, 자기자신 도 아니고 사과도 아닐때
                snake[x][y] = 1
                snake[(x - pos[1][0])][(y - pos[1][1])] = 0

            l_time -= 1
            time += 1
        
    if i[1] == 'D' : #우회전
        if direct == 'u' :
            direct = 'r'
        
        elif direct == 'd' :
            direct = 'l'

        elif direct == 'l' :
            direct = 'u'
        
        elif direct == 'r' :
            direct = 'd'

    elif i[1] == 'L' : #좌회전
        if direct == 'u' :
            direct = 'l'
        
        elif direct == 'd' :
            direct = 'r'

        elif direct == 'l' :
            direct = 'd'
        
        elif direct == 'r' :
            direct = 'u'

    if meet_one == True :
        continue
    else :
        time += 1


print(time)