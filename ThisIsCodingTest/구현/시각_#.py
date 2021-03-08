#완전탐색 : 구현이 중요한 대표적인 문제유형
#탐색해야할 전체 데이터 개수가 100만개 이하일땐 효과적

h = int(input())

count = 0
for i in range(h + 1) :
    for j in range(60) : 
        for k in range(60) :

            if '3' in str(i) + str(j) + str(k) :
                count += 1
print(count)