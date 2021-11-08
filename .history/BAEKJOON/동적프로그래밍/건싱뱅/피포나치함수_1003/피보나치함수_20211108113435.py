zero = [0] * 41
one = [0] * 41

zero[0] = 1
one[0] = 0

zero[1] = 0
one[1] = 1

n = int(input())
TC = []
for i in range(n):
    TC.append(int(input()))

for i in range(n):
    num = TC[i]
    if num == 0 or num == 1:
        print(zero[num], one[num])

    else:
        for i in range(2, num + 1):
            zero[i] = zero[i - 1] + zero[i - 2]
            one[i] = one[i - 1] + one[i - 2]

        print(zero[num], one[num])
