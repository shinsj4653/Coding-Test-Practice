# def fibonacci(n):

#     if n == 0:
#         zero[n] += 1
#         return 0

#     elif n == 1:
#         one[n] += 1
#         return 1

#     else:
#         if d[n] == 0:
#             d[n] = fibonacci(n - 1) + fibonacci(n - 2)
#         return d[n]


zero = [0] * 41
one = [0] * 41

n = int(input())
TC = []
for i in range(n):
    TC.append(int(input()))

for i in range(n):
    num = TC[i]
    for i in range(num + 1):
        zero[i] = zero[i - 1] + zero[i - 2]
        one[i] = one[i - 1] + one[i - 2]

    print(zero[num], one[num])
