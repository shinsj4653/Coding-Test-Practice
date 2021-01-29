ans = []
n = int(input())

while True :

    ans.append(n % 2)
    n = (n // 2)

    if n == 0 :
        break
    

ans.reverse()
#리스트 요소들 그냥 반대로 뒤집을 땐 reverse()
#.sort(reverse = True) 하면 내림차순 정렬의 반대인 오름차순 정렬이됨! 주의

for i in ans :
    print(i, end='')