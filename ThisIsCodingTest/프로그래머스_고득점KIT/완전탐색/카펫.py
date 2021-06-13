import math

def solution(brown, yellow):
    answer = []
    li = [] #약수 넣는 리스트
    
    num = brown + yellow
    
    for i in range(1, int(math.sqrt(num)) + 1) :
        
        if num % i == 0 :
            li.append((i, num // i))
    
    print(li)
    
    for i in range(len(li) - 1, 0, -1) :
        
        if (li[i][0] - 2) * (li[i][1] - 2) == yellow :
            #brown이 한줄씩 감싸고 있기 때문!
            
            answer.append(li[i][1])
            answer.append(li[i][0])
            break
        
    
    
    
    return answer