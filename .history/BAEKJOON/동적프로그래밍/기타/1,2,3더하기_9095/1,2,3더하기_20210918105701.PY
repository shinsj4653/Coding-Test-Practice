n = int(input())
test = []
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(n):
    test.append(int(input()))


for num in test:

    if num < 4:
        print(d[num])

    else:
        d[num] = d[num - 1] + d[num - 2] + d[num - 3]
        print(d[num])

# 인터넷풀이
# 캐치못한 요소 : (4, 1)과 (1, 4)의 경우..
# 어차피 앞의 요소만 고려하니까 4, 1은 가능함.
# 1, 4는 4가 가만히 있음.. -> 그냥 4 사용해서는 표현 불가능!
