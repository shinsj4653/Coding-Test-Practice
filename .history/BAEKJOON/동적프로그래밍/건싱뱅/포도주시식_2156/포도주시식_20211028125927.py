# 연속 3개 불가
# 연속 2개까지는 가능
# n n + 1 , 모두 마시기 아니었으면 개 어려웠을듯

# 첫 시도 -----------------------------------

# n = int(input())
# # wineList = []
# startFirst = []
# startSecond = []
# startThird = []

# sumFirstSec = 0
# sumSecThird = 0
# sumFirstThird = 0

# for i in range(n):
#     wine = int(input())
#     # wineList.append(wine)
#     if i % 3 == 0:
#         startFirst.append(wine)

#     elif i % 3 == 1:
#         startSecond.append(wine)

#     elif i % 3 == 2:
#         startThird.append(wine)


# sumFirstSec = sum(startFirst) + sum(startSecond)
# sumFirstThird = sum(startFirst) + sum(startThird)
# sumSecThird = sum(startSecond) + sum(startThird)

# print(max(sumFirstSec, sumFirstThird, sumSecThird))


# 두번째 시도 -----------------------------------------

# n = int(input())
# wineList = []


# sumFirstOne = 0  # 1, 2 / 1, 2
# sumFirstTwo = 0  # 2, 1/ 2, 1
# sumSecondOne = 0  # 1, 2/1, 2

# for i in range(n):
#     wine = int(input())
#     wineList.append(wine)

# for i in range(n // 3 + 1):

#     if i < n // 3:
#         sumFirstOne += wineList[i * 3] + wineList[i * 3 + 1]
#         sumFirstTwo += wineList[i * 3] + wineList[i * 3 + 2]
#         sumSecondOne += wineList[i * 3 + 1] + wineList[i * 3 + 2]

#     else:
#         if n % 3 == 1:
#             sumFirstOne += wineList[n - 1]
#             sumFirstTwo += wineList[n - 1]

#         elif n % 3 == 2:
#             sumFirstOne += wineList[n - 2] + wineList[n - 1]
#             sumFirstTwo += wineList[n - 2]
#             sumSecondOne += wineList[n - 1]

# print(max(sumFirstOne, sumFirstTwo, sumSecondOne))

# 세 번째 시도 : 1,2,4,6 이렇게 될 수도 있음!!


# def findMax(a, b, c):
#     return max(a, b, c)

# n = int(input())
# wineList = []

# lastIndex = []  # 선택된 와인 위치들
# result = 0

# for i in range(n):
#     wine = int(input())
#     wineList.append(wine)

# num = 0

# for i in range(n // 3 + 1):

#     if i == 0:
#         a = wineList[i]
#         b = wineList[i + 1]
#         c = wineList[i + 2]

#         if a + b > a + c and a + b > b + c:
#             lastIndex.append((i, i + 1))
#             result += a + b

#         elif a + c > a + b and b + c > a + b:
#             lastIndex.append((i + 1, i + 2))
#             result += b + c

#         elif a + c > a + b and a + c > b + c:
#             lastIndex.append((i, i + 2))
#             result += a + c

#     elif i > 0:
#         j = i * 3
#         lastLocation = lastIndex.pop()
#         first = lastLocation[0]
#         second = lastLocation[1]
#         a = wineList[j]
#         b = wineList[j + 1]
#         c = wineList[j + 2]

#         if first == j - 3 and second == j - 2:

#             if a + b > a + c and a + b > b + c:
#                 lastIndex.append((j, j + 1))
#                 result += a + b

#             elif a + b > a + c and b + c > a + b:
#                 lastIndex.append((j + 1, j + 2))
#                 result += b + c
#             else:
#                 lastIndex.append((j, j + 2))
#                 result += a + c

#         elif first == j - 3 and second == j - 1:

#             if a + b > a + c and b + c > a + b:
#                 lastIndex.append((j + 1, j + 2))
#                 result += b + c
#             else:
#                 lastIndex.append((j, j + 2))
#                 result += a + c

#         elif first == j - 2 and second == j - 1:

#             lastIndex.append((j + 1, j + 2))
#             result += b + c

# print(result)

# 마지막 시도 -----------------------------------
n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))

dp = [0]
dp.append(w[1])
if n > 1:
    dp.append(w[1] + w[2])

# 해당 순서의 포도주를 마시지 않는 경우/마신다면 전거를 마신 경우와 안 마신 경우
