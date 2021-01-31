#절댓값 기준으로 이웃 끼리의 숫자만 확인하면 된다.

import math 

N = int(input())
l = list(map(int, input().split()))
ans = []
min_l = 21000000000
first = 100001
second = 100001
l.sort(key = lambda x : abs(x))

for i in range(N - 1) : 
        
        if min_l > abs(l[i] + l[i + 1]) :
            min_l = abs(l[i] + l[i + 1])
            first = l[i]
            second = l[i + 1]

if first < second : 
    print(first,second)
else : 
    print(second,first)