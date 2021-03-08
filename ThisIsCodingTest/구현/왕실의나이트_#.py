#for문 안에서는 일정하게 변경되는 값만 넣기
#불규칙적으로 좌표가 변경되면 dx dy 리스트 제작

place = input()

#열
col = ord(place[0]) - 96

#행
row = int(place[1])

print(col,row)

count = 0

#열
dx = [2, 2, 1, -1, -2, -2, 1, -1] 

#행
dy = [1, -1, 2, 2, 1, -1, -2, -2]

for i in range(8) :

    nx = col + dx[i]
    ny = row + dy[i]

    if nx > 8 or ny > 8 or nx < 1 or ny < 1 :
        continue

    count += 1

print(count)

#steps변수가 dx dy 기능을 대신 수행
#위의 dx dy와 steps 좌표 둘 다 자주 사용됨.

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for step in steps : #좌표 하나하나 가져오기

    next_row = row + step[0]
    next_col = col + step[1]


