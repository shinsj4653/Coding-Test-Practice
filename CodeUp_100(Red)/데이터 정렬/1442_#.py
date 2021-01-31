#선택정렬  : 모든 index에 대해서 그 index에 위치시킬 값을 '선택'하기 때문에 선택정렬
#각 index에서 대해서 최솟값을 찾기 위해 대소비교는 여러번 일어나나 상호교대는 딱 한번 일어남.
#시간 복잡도 : O(N^2)
n = int(input())
a = []
for i in range(n) :
    a.append(int(input()))


for i in range(0, n - 1) : 
    min_index = i
    for j in range(i + 1, n) :
        
        if a[min_index] > a[j] :
            min_index = j

    a[min_index] , a[j] = a[j], a[min_index]
    
for i in range(n) :
    print(a[i])

#선택정렬 최적화 ->x

