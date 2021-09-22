a, b, c = map(int, input().split())
multiplyList = [(a, b)]  # (0, 1) -> 곱할 수, 곱할 횟수


def multiply(b):

    lastIndex = len(multiplyList) - 1

    num, multiplyCount = multiplyList[lastIndex]

    if multiplyCount == 2 :
        multiplyList[lastIndex][0] = num * num
        multiplyList[lastIndex][1] = 1
        
    elif multiplyCount == 1 :
        

    elif multiplyCount % 2 != 0:
        multiplyList[0][1] = multiplyCount % 2
        num = num * num
        b = multiplyCount // 2
        multiplyList.append((num, b))

        multiply(b // 2)


multiply(a, b)
