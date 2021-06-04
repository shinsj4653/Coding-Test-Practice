#핵심아이디어 : 파라메트릭 서치 -> 최적화 문제를 결정 문제(yes or no로 답변가능)로 바꾸어 해결하는 기법.
#파라메트릭 서치는 이진탐색활용
#절단기의 적절한 높이를 찾을때까지 높이H를 조정하는 것.
#절단기의 높이 자체의 범위 -> 1부터 10억이라는 큰 수->당연히 이진탐색 떠올리기.
#절단기의 높이를 이진탐색을 활용하여 1부터 10억사이에서 찾는것임. 리스트에 정해진 답을 찾는 방식으로 떠올리면x

#절단기의 높이 -> 0부터 가장 긴 떡의 길이 안에 있어야한다.

#떡들의 높이 리스트에 집중 x -> 답은 절단기의 높이를 찾는 것이여서 절단기의 높이에 집중!!

n, m = map(int, input().split())

ddok = list(map(int, input().split()))

start = 0
end = max(ddok)

result = 0

while start <= end :
    total = 0
    mid = (start + end) // 2
    for x in ddok :

        if x > mid :
            total += x - mid

    if total < m : #더 많은 떡 필요. -> 절단면의 높이를 감소
        end = mid - 1

    else : #떡이 너무 많음 -> 절단면 높이 증가
        start = mid + 1
        result = mid #얻을 수 있는 떡의 길이 합이 필요한 떡의 길이보다 크거나 같을 때마다 mid값으로 갱신!

#total값을 비교한다는 조건을 추가로 건 이진탐색!

print(result)

