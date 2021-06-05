key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def turn(key) :

    new_key = [[0] * 3 for _ in range(3)]
    i = 0

    for keys in key :
    
        for j in range(3) :
            new_key[j][2 - i] = keys[j]
        
        i += 1

    return new_key

while True :

    for i in range(3) :
        for j in range(3) :
            
            if key[i][j] == 1 :
                if lock[i][j] == 1 : #키가 락 홈에 맞지 않을때
                    key = turn(key)
                
                else : #키가 락 홈에 맞을때
                    
                


    
    