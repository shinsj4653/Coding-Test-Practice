import heapq

a, b, c = map(int, input().split())
multiplyList = []
heapq.heappush(multiplyList, (a, b))  # (0, 1) -> 곱할 수, 곱할 횟수
resultList = []

while True:

    num, multiplyCount = heapq.heappop(multiplyList)

    if multiplyCount == 2:
        multiplyList[lastIndex][0] = num * num
        multiplyList[lastIndex][1] = 1
        break

    else:
        if multiplyCount % 2 != 0:
            resultList.append(num)
            num = num * num
            b = multiplyCount // 2
            multiplyList.append((num, b))

        else:
            num *= num
            multiplyCount //= 2
            multiplyList[lastIndex][1] = b

for num in multiplyList:
    result *= num[0]

print(result)
