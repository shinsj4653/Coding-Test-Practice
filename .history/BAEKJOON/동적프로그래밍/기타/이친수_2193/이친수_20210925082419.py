n = int(input())
d = [0] * 91
d[1] = 1  # 1
# 0
d[2] = 1  # 10
# 00 01
d[3] = 2  # 100, 101
# 000 001 010
# 4 : 1000 1001 1010
# 0000, 0001, 0010, 0100, 0101
# 5 : 10000, 10001, 10010, 10100, 10101


for i in range(4, n + 1):
    d[i] = d[i - 1] + (d[i - 1] + 1)
