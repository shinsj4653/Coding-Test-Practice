n = int(input())
result = 0

while True :
    if (n % 5) % 3 == 0 : #5로 나눈 나머지가 3의 배수 일때
        result = n // 5 + (n % 5) // 3
        break

    else : #아닐떄
        if n > 5 :
            n -= 5

        else :
            if n == 3 :
                result = 1
                break
            else :
                result = -1
                break
    
    if n % 3 == 0 :
        
            
print(result)