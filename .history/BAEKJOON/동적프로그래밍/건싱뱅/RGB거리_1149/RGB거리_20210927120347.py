# n = int(input())
# cost = []
# for i in range(n):
#     cost.append(list(map(int, input().split())))

# colorStart = cost[0].index(min(cost[0]))
# resultStart = 0
# resultStart += cost[0][colorStart]

# colorLast = cost[n - 1].index(min(cost[n - 1]))
# resultLast = 0
# resultLast += cost[n - 1][colorLast]

# for i in range(1, n):

#     if colorStart == 0:
#         colorStart = cost[i].index(min(cost[i][1], cost[i][2]))
#         resultStart += cost[i][colorStart]

#     elif colorStart == 1:
#         colorStart = cost[i].index(min(cost[i][0], cost[i][2]))
#         resultStart += cost[i][colorStart]

#     elif colorStart == 2:
#         colorStart = cost[i].index(min(cost[i][0], cost[i][1]))
#         resultStart += cost[i][colorStart]

#     if colorLast == 0:
#         colorLast = cost[n - i - 1].index(min(cost[n - i - 1][1], cost[n - i - 1][2]))
#         resultLast += cost[n - i - 1][colorLast]

#     elif colorLast == 1:
#         colorLast = cost[n - i - 1].index(min(cost[n - i - 1][0], cost[n - i - 1][2]))
#         resultLast += cost[n - i - 1][colorLast]

#     elif colorLast == 2:
#         colorLast = cost[n - i - 1].index(min(cost[n - i - 1][0], cost[n - i - 1][1]))
#         resultLast += cost[n - i - 1][colorLast]

# print(min(resultStart, resultLast))

# 윗 방법 : 실패라고 나옴

n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))
dR = [0] * n
dG = [0] * n
dB = [0] * n
result = 0

if cost[0].index(min(cost[0])) == 0:
    dR[0] = 1

elif cost[0].index(min(cost[0])) == 1:
    dG[0] = 1

else:
    dB[0] = 1


for i in range(1, n):
    if dR[i - 1] != 0:
        cost[i][0] = 0
