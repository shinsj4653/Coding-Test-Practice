#원래의 배열을 한줄씩 늘려서 모든 칸에서 주변 8칸 탐색가능하도록
g = []
old_g = [[0] * 26 for _ in range(26)]

for i in range(25) : 
    g.append(list(map(int, input().split())))

for i in range(25) :
    for j in range(25) :
        old_g[i][j] = g[i][j]

next_g = [[0] * 25 for _ in range(25)]

for i in range(25) :
    for j in range(25) :

        if old_g[i][j] == 0 : 
            life = 0 
            for x in range(i - 1, i + 2) :
                for y in range(j - 1, j + 2) :
                    
                    if x == i and y == j :
                        continue
                    else : 
                        if old_g[x][y] == 1 :
                            life += 1
                
            if life == 3 :
                next_g[i][j] = 1

        
        elif old_g[i][j] == 1 : 
            life = 0


            for x in range(i - 1, i + 2) :
                for y in range(j - 1, j + 2) :
                    
                    if x == i and y == j :
                        continue
                    else : 
                        if old_g[x][y] == 1 :
                            life += 1

            if life >= 4 or life <= 1 :
                next_g[i][j] = 0
            elif life == 2 or life == 3 : 
                next_g[i][j] = 1

for i in range(25) :
    for j in range(25) :
        print(next_g[i][j], end = " ")
    print()
