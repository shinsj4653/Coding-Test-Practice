n, k = map(int, input().split())
a = [] #리스트 선언필요x
b = []
#최대 k번 바꿔치기 가능.
#함정 : 교환할때 배열a에서의 가장 작은원소가 배열b에서의 가장 큰 원소보다 작을 때에만 교체를 수행해야함.

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# for i in range(k) :

#     a_min = min(a)
#     a_index = a.index(a_min)

#     b_max = max(b)
#     b_index = b.index(b_max)

#     a[a_index], b[b_index] = b[b_index], a[a_index]
a.sort()
b.sort(reverse=True)

count = 1
i = 0

for i in range(k) :

    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
    else :
        break #정렬된 원소들이라 만약 a가 더 크면 b의 원소들은 더 이상 볼 필요x

print(sum(a))
#리스트의 모든원소합 : sum()함수활용