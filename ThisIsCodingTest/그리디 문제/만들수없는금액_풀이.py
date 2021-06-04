#정렬까지는 잘 떠올림
#target변수를 업데이트 시키는 방식을 활용해야함.
#화폐단위만큼 더하면서 업데이트 -> 더했을 때, 그보다 이하의 값들은 만들 수 있는 금액
#target보다 크면, 만들 수 없음

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data :
    
    if target < x :
        break

    target += x

print(target)
