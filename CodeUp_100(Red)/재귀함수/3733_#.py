a, b = map(int, input().split())
obak = [0] * 10000001
obak[1] = 4
obak[2] = 2
obak[4] = 3

def f_obak(k) :

    if not obak[k] :

        if k % 2 != 0 :
            obak[k] = 1 + f_obak(3 * k + 1)
            return obak[k]


        elif k % 2 == 0 :
            obak[k] = 1 + f_obak(k // 2)
            return obak[k]
    else : 
        return obak[k]   

for i in range(a, b + 1) :
    obak[i] = f_obak(i)

max_obak = 0
max_len = 0

for i in range(a, b + 1) :
    
    if max_len < obak[i] : 
        max_obak = i
        max_len = obak[i]

print(max_obak,max_len)

#테스트 케이스 11275 8400510 에서 오류..
#풀이
#배열을 천만까지만 잡고 더 큰 숫자가 재귀될 때는 그냥 메모이제이션을 하지 않는것.
a, b = map(int, input().split())
obak = [0] * 10000001

def f_obak(k) :

    if k == 1 :
        return 1

    if k > 10000000 : #천만이 넘는 큰 수라면(메모 배열 넘음) 메모안함
        if k % 2 == 0 :
            return f_obak(k // 2) + 1
        else :
            return f_obak(3 * k + 1) + 1
        
    if obak[k] != 0 :
        return obak[k]

    else :
        if k % 2 == 0 :
            obak[k] = f_obak(k // 2) + 1
            return obak[k]
        else :
            obak[k] = f_obak(3 * k + 1) + 1
            return obak[k]



max_obak = 0
max_len = 0

for i in range(a, b + 1) :
    
    obak[i] = f_obak(i)

    if max_len < obak[i] : 
        max_obak = i
        max_len = obak[i]

print(max_obak,max_len)