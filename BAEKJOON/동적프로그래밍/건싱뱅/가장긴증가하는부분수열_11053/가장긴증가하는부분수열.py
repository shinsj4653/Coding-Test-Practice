# n = int(input())
# length = 0

# A = list(map(int, input().split()))
# max_num = A[0]

# for i in range(len(A)):

#     if max_num < A[i]:
#         max_num = A[i]
#         length += 1

#     else:
#         A[i] = max_num

# print(length)

# 포기 -> 인터넷 풀이
x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
