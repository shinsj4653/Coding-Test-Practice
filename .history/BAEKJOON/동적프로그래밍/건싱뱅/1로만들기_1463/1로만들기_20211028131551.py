x = int(input())
dp = [0] * (x + 1)
dp[0] = 0
dp[1] = 0
dp[2] = 1  # -1만 해주면 됨
dp[3] = 1  # 나누기 3만 해주면 됨

for i in range(4, x + 1):
    if i % 2 == 0:
        dp[i] = i // 2

    elif i % 3 == 0:
        dp[i] = i // 3

    else:
        dp[i] = 1 + dp[i - 1]
