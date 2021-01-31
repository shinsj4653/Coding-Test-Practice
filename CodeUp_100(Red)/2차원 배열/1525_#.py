#append 함수 : 무조건 하나의 type만 가져감.
#new_crazy = crazy : 배열 이름 대입하면 new_crazy도 crazy를 가리켜서 new_crazy 값 변경하면 crazy 값도 같이 변경됨.

crazy = []
for i in range(10) :
    crazy.append(list(map(int, input().split())))

new_crazy = [[0] * 10 for _ in range(10)]
for i in range(10) :
    for j in range(10) :
        new_crazy[i][j] = crazy[i][j]

for i in range(10) :
    for j in range(10) :

        if crazy[i][j] >= 1 :
            num = 0
            num = crazy[i][j]
            new_crazy[i][j] = -2
            direct = 0

            while direct < 4 :

                
                for bub in range(1, num + 1) :
                    

                    if direct == 0 : #위

                        if i - bub >= 0 :
        
                            if crazy[i - bub][j] == -1:
                                break
                            else :
                                new_crazy[i - bub][j] = -2

                    elif direct == 1 :#오른
                        
                        if j + bub <= 9 :

                            if crazy[i][j + bub] == -1:
                                break
                            else : 
                                new_crazy[i][j + bub] = -2

                
                    elif direct == 2 :#아래

                        if i + bub <= 9 :
        
                            if crazy[i + bub][j] == -1:
                                break
                                
                            else :
                                new_crazy[i + bub][j] = -2
                
                    elif direct == 3 :#왼

                        if j - bub >= 0 :

                            if crazy[i][j - bub] == -1:
                                break
                            else : 
                                new_crazy[i][j - bub] = -2 
                
                direct += 1

n = int(input())

player = []

for i in range(n) :
    a, b = map(int, input().split())
    x = a - 1
    y = b - 1
    if new_crazy[x][y] == 0 :
        new_crazy[x][y] = i + 1
        player.append("player "+str(i + 1)+" survive")
    else : 
        player.append("player "+str(i + 1)+" dead")

for i in range(10) :
    for j in range(10) :
        print(new_crazy[i][j], end = " ")
    print()

print("Character Information")
for i in range(len(player)) :
    print(player[i])