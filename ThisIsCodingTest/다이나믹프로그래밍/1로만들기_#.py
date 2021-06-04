x = int(input())
d = [0] * 30001 # 횟수 저장 배열 -> 수의 범위가 1부터 30000이면 30000까지 인덱스 필요 -> 배열크기는 30001

#횟수의 최솟값 : min()함수 이용
for i in range(2, x + 1) :
    d[i] = d[i - 1] + 1

    if i % 2 == 0 :
        d[i] = min(d[i], d[i // 2] + 1)

    elif i % 3 == 0 :
        d[i] = min(d[i], d[i // 3] + 1)

    elif i % 5 == 0 :
        d[i] = min(d[i], d[i // 5] + 1)



print(d[x])

