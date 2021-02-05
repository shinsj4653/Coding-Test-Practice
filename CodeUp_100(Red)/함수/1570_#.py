#주요 라이브러리 문법
#정렬된 배열이 들어왔을때 삽입할 원소 위치 찾기. -> bisect : bisect_left, bisect_right
from bisect import bisect_left
global n, k, d

def lower_bound(k) :

    return bisect_left(d, k) + 1
    
    

n = int(input())
d = list(map(int, input().split()))
k = int(input())
print(lower_bound(k))