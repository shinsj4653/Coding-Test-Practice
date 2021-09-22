a, b, c = map(int, input().split())
multiplyList = []


def multiply(a, b):

    for i in range(b // 2):
        multiplyList.append(a ** a)


multiply(a, b)
