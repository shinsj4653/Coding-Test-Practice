#버블정렬
#python은 swap할때 변수 자리 바꿔서 대입하면됨.
#i의 시작을 len(a) - 1 부터 해서 점점 줄여나가야함.
#시간 복잡도 : O(N^2)

# a = []
# n = 0 
# i = 0
# temp = 0
# n = int(input())

# for i in range(1, n + 1) :
#     a.append(int(input()))

# for i in range(len(a) - 1, 0, -1) :
    
#     for j in range(i) :
        
#         if a[j] > a[j + 1] :

#             a[j], a[j + 1] = a[j + 1], a[j]

# for i in range(n) :
#     print(a[i])

#시간 초과해결 -> 최적화
#이전 패스에서 앞뒤 자리 비교가 한번도 일어나지 않았다면 다 정렬되어 있다고 할 수 있음.


# a = []
# n = 0 
# i = 0
# temp = 0
# n = int(input())

# for i in range(1, n + 1) :
#     a.append(int(input()))

# for i in range(len(a) - 1, 0, -1) :
    
#     swap = False
#     for j in range(i) :
        
#         if a[j] > a[j + 1] :

#             a[j], a[j + 1] = a[j + 1], a[j]
#             swap = True

#     if not swap : 
#         break

# for i in range(n) :
#     print(a[i])

#추가 최적화
#이전 단계에서 앞뒤 자리 비교가 있었던 index를 기억해두면 다음 차례에선 그 자리 전까지만 정렬해도 된다.

a = []
n = 0 
i = 0
temp = 0
n = int(input())

for i in range(n) :
    a.append(int(input()))

end = len(a) - 1

while end > 0 :
    last_swap = 0
    for i in range(end) :
        if a[i] > a[i + 1] :
            a[i], a[i + 1] = a[i + 1], a[i]
            last_swap = i
        
    end = last_swap
    

for i in range(n) :
    print(a[i])