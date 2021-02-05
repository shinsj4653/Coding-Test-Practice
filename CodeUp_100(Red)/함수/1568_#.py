#최댓값, 최솟값 잘 구분하기
global n, a, b, d

def maxi(a, b) :

    max_num = -2147483648
    max_i = 0
    for i in range(a - 1, b) :
        if max_num < d[i] :
            max_num = d[i]
            max_i = i
    
    return max_i + 1
            


n = int(input())
d = list(map(int, input().split()))
a, b = map(int, input().split())



print(maxi(a, b))
