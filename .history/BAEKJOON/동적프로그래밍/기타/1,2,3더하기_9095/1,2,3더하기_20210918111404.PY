from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

n = int(input())
test = []
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4


for i in range(n):
    test.append(int(input()))


def plus(n):
    if d[n] != 0:
        return d[n]

    else:
        d[n] = plus(d[n - 1]) + plus(d[n - 2]) + plus(d[n - 3])
        return d[n]


for i in range(n):
    num = test[i]
    print(plus(num))

# 인터넷풀이
# 캐치못한 요소 : (4, 1)과 (1, 4)의 경우..
# 어차피 앞의 요소만 고려하니까 4, 1은 가능함.
# 1, 4는 4가 가만히 있음.. -> 그냥 4 사용해서는 표현 불가능!
