# 정수삼각형 1932 랑 유사
# 배열안의 값들을 차례대로 누적해가면서 값을 업데이트해 나가는 방식
# 이전의 값들을 차례대로 활용 -> 다이나믹 프로그래밍

## -------------------------------

# n = int(input())
# cost = []
# for i in range(n):
#     cost.append(list(map(int, input().split())))

# index = cost[0].index(min(cost[0]))

# result = 0
# result += cost[0][index]

# for i in range(1, n):

#     if index == 0:
#         cost[i][index] = 10000

#     elif index == 1:
#         cost[i][index] = 10000

#     elif index == 2:
#         cost[i][index] = 10000

#     result += min(cost[i])
#     index = cost[i].index(min(cost[i]))

# print(result)
## -------------------------------
# 따로 result변수에 저장하는게 아니라, 이전 계산값을 저장해서 다음 계산에 그대로 활용


n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))


# 반대로 계산 하는경우 -> 집을 칠하는 순서가 주어져 있음! -> 반대로 계산하는 경우는 존재X
# for i in range(n):
#     dR[i] = 0
#     dG[i] = 0
#     dB[i] = 0

# if costEnd[n - 1].index(min(costEnd[n - 1])) == 0:
#     dR[n - 1] = 1

# elif costEnd[n - 1].index(min(costEnd[n - 1])) == 1:
#     dG[n - 1] = 1

# else:
#     dB[n - 1] = 1
# resultEnd += min(costEnd[n - 1])

# for i in range(n - 2, -1, -1):
#     if dR[i + 1] == 1:
#         costEnd[i][0] = INF

#     elif dG[i + 1] == 1:
#         costEnd[i][1] = INF

#     else:
#         costEnd[i][2] = INF

#     if costEnd[i].index(min(costEnd[i])) == 0:
#         dR[i] = 1

#     elif costEnd[i].index(min(costEnd[i])) == 1:
#         dG[i] = 1

#     else:
#         dB[i] = 1
#     resultEnd += min(costEnd[i])

# print(min(result, resultEnd))
