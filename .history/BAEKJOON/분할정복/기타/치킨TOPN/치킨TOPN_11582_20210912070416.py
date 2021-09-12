n = int(input())
chicken = list(map(int, input().split()))
k = int(input())

count = n // 2  # 정렬을 하는 사람의 수
mergeCount = 0

while True:
    loopCount = count
    mergeCount = n // count

    for i in range(loopCount):
        chicken[i * mergeCount : i * mergeCount + mergeCount] = sorted(
            chicken[i * mergeCount : i * mergeCount + mergeCount]
        )

    # 마지막에 if count == k 이면 break
    if count == k:
        break

    count //= 2

print(every c in chicken)
