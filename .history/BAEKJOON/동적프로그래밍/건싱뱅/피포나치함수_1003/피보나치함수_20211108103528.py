def fibonacci(n):

    if n == 0:
        print("0")
        return 0

    elif n == 1:
        print("1")
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


zeroCount = 0
oneCount = 0

n = int(input())
TC = []
for i in range(n):
    TC.append(int(input()))
