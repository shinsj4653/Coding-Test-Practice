a, b, c = map(int, input().split())
multiplyList = [(a, b)]  # (0, 1) -> 곱할 수, 곱할 횟수


def multiply(a, b):

    num, multiplyCount = multiplyList[0]

    if b % 2 != 0:
        multiplyList[0][1] = multiplyCount % 2
        a = a * a
        multiplyList.append(a, (multiplyCount // 2))

    multiply(a, b // 2)


multiply(a, b)
