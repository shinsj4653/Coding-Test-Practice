a, b, c = map(int, input().split())
multiplyNum = 1


def multiply(a, b):

    global multiplyNum

    if b % 2 == 0:
        for i in range(b // 2):
            multiplyNum *= a

    else:
        for i in range(b // 2):
            multiplyNum *= a

        multiplyNum *= a


multiply(a, b)
