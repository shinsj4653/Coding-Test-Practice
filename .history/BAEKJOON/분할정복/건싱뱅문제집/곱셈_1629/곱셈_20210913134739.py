a, b, c = map(int, input().split())
multiplyList = [(a, b)]  # (0, 1) -> 곱할 수, 곱할 횟수


def multiply(a, b):

    lastIndex = len(multiplyList) - 1

    num, multiplyCount = multiplyList[lastIndex]

    if multiplyCount == 2:
        multiplyList[lastIndex][0] = num * num

    elif multiplyCount % 2 != 0:
        multiplyList[0][1] = multiplyCount % 2
        a = a * a
        b = multiplyCount // 2
        multiplyList.append((a, b))

        multiply(a, b // 2)


multiply(a, b)
