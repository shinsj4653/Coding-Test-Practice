import sys 

maze = []
for i in range(10) :
    line = list(map(int, input().split()))
    maze.append(line)
x = 1
y = 1
def show_maze() : 
    for i in range(10) :
        for j in range(10) :
            print(maze[i][j], end = " ")
        print("")

while(True) :

    #첨에 바로 발견했을 때
    if(maze[x][y] == 2) :
        maze[x][y] = 9
        show_maze()
        sys.exit()

    maze[x][y] = 9
    #못 움직이는 경우
    if (maze[x][y + 1] == 1 and maze[x + 1][y] == 1) or (x == 8 and y == 8) :
        #print("break")
        show_maze()
        sys.exit()
    #움직이는 경우
    elif maze[x][y + 1] == 2 :
        #rint("found")
        maze[x][y + 1] = 9
        show_maze()
        sys.exit()
    elif maze[x][y + 1] != 2 and maze[x][y + 1] == 0 :
        #print("right")
        maze[x][y] = 9
        y = y + 1

    elif maze[x][y + 1] != 2 and maze[x][y + 1] != 0 and maze[x + 1][y] == 2 :
        #print("found")
        maze[x + 1][y] = 9
        show_maze()
        sys.exit()

    elif maze[x][y + 1] != 2 and maze[x][y + 1] != 0 and maze[x + 1][y] != 2 and maze[x + 1][y] == 0:
        #print("down")
        maze[x + 1][y] = 9
        x = x + 1


#풀이2 -> while문
#움직이는 방향 : 오른쪽, 그다음에 아래로 -> 문제 조건 명확히 두고 풀기.
while True :
    if m[x][y]==0 :
        m[x][y]=9
    elif m[x][y]==2 :
        m[x][y]=9
        break

    if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) :
        break

    if m[x][y+1]!=1 : #기준을 숫자로도 세팅해보기
        #2거나 0이거나 둘다 1이 아니고, 1이 아닐때 이동한다.
        y+=1#이동한다 라는 행위가 어떤 조건에서 실행되는지 생각 -> 0 또는 2일때 -> 이것보단 그냥 1이 아닐때가 더 적합.
    elif m[x+1][y]!=1 :
        x+=1

