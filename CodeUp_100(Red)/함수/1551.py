global n
global d
global k

def f(k) :

    for num in d :
        if num == k :
            return d.index(num) + 1
    
    return -1
        


n = int(input())

d = list(map(int, input().split()))

k = int(input())



print(f(k))