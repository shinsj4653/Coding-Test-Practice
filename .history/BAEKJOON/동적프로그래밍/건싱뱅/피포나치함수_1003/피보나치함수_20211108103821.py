def fibonacci(n):

    global zeroCount
    global oneCount

    if n == 0:
        print("0")
        zeroCount += 1
        return 0

    elif n == 1:
        print("1")
        oneCount += 1
        return 1

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


global zeroCount
global oneCount

zeroCount = 0
oneCount = 0


n = int(input())
TC = []
for i in range(n):
    fibonacci(int(input()))
    print(zeroCount,oneCount)
    

