#방향을 설정해서 이동하는 문제 유형에서는  dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적
#반복문을 사용하여 모든 방향을 차례대로 확인가능
n, m = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())

d[x][y] = 1

array = []
for i in range(n) : 
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

def turn_left() :
    global direction #전역변수를 함수에서 사용하기 위해선 global 키워드 필요
    direction -= 1

    if direction == -1 :
        direction = 3

count = 0
turn_time = 0

while True :

    turn_left()

    nx = x + dx[direction] #방향을 인덱스로 활용하는 아이디어
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else : 
        turn_time += 1

    if turn_time == 4 :
        nx = x - dx[direction]
        ny = y - dx[direction]

        if array[nx][ny] == 0 :
            x = nx
            y = ny
            count += 1
        
        else : 
            break
        turn_time = 0

print(count)
    

# n, m = map(int, input().split())
# x, y, direct = map(int, input().split())
# #x : 행
# #y : 열
# a = 0
# b = 0
# count = 0

# def change(direct, x, y) :

#     newx = 0
#     newy = 0

#     if direct == 0 : #북
#         newx = x - 1
#         newy = y

#     elif direct == 1 : #동
#         newx = x
#         newy = y - 1

#     elif direct == 2 : #서
#         newx = x
#         newy = y + 1

#     elif direct == 3 : #남
#         newx = x + 1
#         newy = y 
    
#     return newx, newy


# land = []

# for i in range(n) :
#     land.append(list(map(int, input().split())))

# if direct < 3 :
#     direct += 1
#     a, b = change(direct, x, y)
    
# elif direct == 3 :
#     direct = 0
#     a, b = change(direct, x, y)

# turn = 0 #회전한 횟수

# while True :

#     if land[a][b] == 0 : #방문안한 육지
#         x = a
#         y = b
#         count += 1
#         land[a][b] == 2#방문

#         a, b = change(direct, x, y)

#     elif land[a][b] == 1 or land[a][b] == 2 : #바다거나 방문이미 한땅

#         if turn < 4 :
            
#             if direct < 3 :
#                 direct += 1
#                 a, b = change(direct, x, y)
    
#             elif direct == 3 :
#                 direct = 0
#                 a, b = change(direct, x, y)

#             turn += 1

#         elif turn == 4 : #4방향 모두 방문 or 바다
#             turn = 0

#             if direct == 0 : #북 바라보고 있으니 남쪽으로 뒤로 가야함.
                
#                 x = x + 1

#             elif direct == 1 : #동 바라보고있으니 서쪽으로 뒤로 가야
                
#                 y = y + 1
            
#             elif direct == 2 : #남 바라보고 있으니 북으로 뒤로가야

#                 x = x - 1
             
#             elif direct == 3 : #서 바라보고 있으니 동으로 뒤로가야

#                 y = y - 1
            
            
#             if land[x][y] == 1 :
#                 break
            
#             else : 
#                 count += 1
#                 if direct < 3 :
#                     direct += 1
#                     a, b = change(direct, x, y)
    
#                 elif direct == 3 :
#                     direct = 0
#                     a, b = change(direct, x, y)

# print(count)
        

        


    
        
    



