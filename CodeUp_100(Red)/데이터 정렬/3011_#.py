#버블 소트 최적화
a = []
n = 0 
i = 0
temp = 0
ans = 0
n = int(input())

a = list(map(int, input().split()))

for i in range(len(a)) :
    
    swap = False
    for j in range(len(a) - i - 1) :
        
        if a[j] > a[j + 1] :

            a[j], a[j + 1] = a[j + 1], a[j]
            swap = True

    if not swap : 
        ans = i
        break

print(ans)