a, b, c = map(int, input().split())
multiplyNum = 1


def multiply(a, b):

    global multiplyNum
    if 

    if b % 2 == 0:
        for i in range(b // 2):
            multiplyNum *= a ** 2

    else:
        for i in range(b // 2):
            multiplyNum *= a ** 2

        multiplyNum *= a
    
    multiply(a ** 2, b // 2)


multiply(a, b)
