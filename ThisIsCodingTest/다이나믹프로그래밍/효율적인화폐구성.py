n, m = map(int, input().split())
#금액크기만큼 리스트 할당 -> 메모이제이션 활용
#화폐 단위당 사이클을 또 돌려서(2중 반복문), 일일히 확인.

array = []
for i in range(n) :
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n) :
    for j in range(array[i], m + 1) :
        if d[j - array[i]] != 10001 :
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001 :
    print(-1)

else :
    print(d[m])
