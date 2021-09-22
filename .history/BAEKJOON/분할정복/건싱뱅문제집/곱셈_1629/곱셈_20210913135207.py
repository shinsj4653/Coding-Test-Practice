a, b, c = map(int, input().split())
multiplyList = [(a, b)]  # (0, 1) -> 곱할 수, 곱할 횟수


while True:

    lastIndex = len(multiplyList) - 1

    num, multiplyCount = multiplyList[lastIndex]

    if multiplyCount == 2:
        multiplyList[lastIndex][0] = num * num
        multiplyList[lastIndex][1] = 1
        break

    if multiplyCount > 2:
        if multiplyCount % 2 != 0:
            multiplyList[0][1] = multiplyCount % 2
            num = num * num
            b = multiplyCount // 2
            multiplyList.append((num, b))

        else:
            multiplyList[lastIndex][0] = num * num
            b = multiplyCount // 2
            multiplyList[lastIndex][1] = b
