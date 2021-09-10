n, m = map(int, input().split())
l = []
for i in range(n) :
    new_l = list(map(int, input().split()))
    l.append(new_l)

max_num = 0 #최대 최소 헷갈리지 않게 문제에서 잘 캐치하기

for i in range(n) :
    
    small_l = []
    small_l = l[i]
    #small_l.sort()
    #sort() 대신 list에서 가장 작은 값을 반환하는 min()함수 사용!
    num = min(small_l)

    if num > max_num :
        max_num = num

print(max_num)

#좀 더 간결한 책풀이
n, m = map(int, input().split())

result = 0

for i in range(n) :
    data = list(map(int, input().split()))

    min_value = min(data) # 한 줄씩 확인하여 값을 제때제때 업데이트!!
    # 초기화 되어도 상관x

    result = max(result, min_value)

print(result)
