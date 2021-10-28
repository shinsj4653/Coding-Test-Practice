x = int(input())
dp = [0] * (x + 1)
dp[0] = 0
dp[1] = 0
dp[2] = 1  # -1만 해주면 됨
dp[3] = 1  # 나누기 3만 해주면 됨
if x > 3 :
    for i in range(4, x + 1):
    
    if i % 6 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1)

    elif i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)

    elif i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)

    else:
        dp[i] = dp[i - 1] + 1

print(dp[x])

# 어떤 예외가 있는거지????
