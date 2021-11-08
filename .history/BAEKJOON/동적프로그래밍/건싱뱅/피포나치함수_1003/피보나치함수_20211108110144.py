def fibonacci(n):

    print("0 : ", zeroCount)
    print("1 : ", oneCount)

    if n == 0:
        count[0] += 1
        return 0

    elif n == 1:
        count[1] += 1
        return 1

    else:
        if d[n] == 0:
            d[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return d[n]


d = [0] * 41
d[1] = 1

count = [0, 0]

n = int(input())
TC = []
for i in range(n):
    TC.append(int(input()))

for i in range(n):
    fibonacci(TC[i])
    print(zeroCount, oneCount)
    zeroCount = 0
    oneCount = 0
