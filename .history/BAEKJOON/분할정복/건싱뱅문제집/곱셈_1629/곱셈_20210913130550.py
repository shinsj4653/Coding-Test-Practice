a, b, c = map(int, input().split())
multiplyList = []

if b % 2 == 0:
    for i in range(b // 2):
        multiplyList.append(a ** a)

print((a ** b) % c)
