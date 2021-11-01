# x = int(input())
# dp = [0] * (x + 1)
# dp[0] = 0
# dp[1] = 0 -> 애초에 0으로 초기화 된 상태 : 필요x
# dp[2] = 1  # -1만 해주면 됨
# dp[3] = 1  # 나누기 3만 해주면 됨

# for i in range(2, x + 1):

#     if i % 6 == 0:
#         dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1)

#     elif i % 3 == 0:
#         dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)

#     elif i % 2 == 0:
#         dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)

#     else:
#         dp[i] = dp[i - 1] + 1

# 6의 배수일때를 한꺼번에 고려하는 방법 : if만 사용
x = int(input())
dp = [0] * (x + 1)
for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])

    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])


print(dp[x])

# 어떤 예외가 있는거지???? -> 공배수! 2와 3 : 6의 배수일때도 고려해야
