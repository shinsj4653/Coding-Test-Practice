zero = [0] * 41
one = [0] * 41

zero[0] = 1
one[0] = 0

zero[1] = 0
one[1] = 1

# 1 2 3 4 5 6 7 -> 3 일때 1,2 / 4 일때 2,3 -> 그 단계와 그 전 단계의 피보나치 값들을 출력하면 됨
# 1 1 2 3 5 8 13

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

# ------------- 인터넷 풀이 --------------
t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)
