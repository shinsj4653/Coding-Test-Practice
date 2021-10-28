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
n = int(input())
wineList = []
selectedWine = [] # 선택된 와인 위치들
result = 0

for i in range(n):
    wine = int(input())
    wineList.append(wine)
    
for i in range(n // 3 + 1) :
    if i == 0:
        if(max(wineList[i] + wineList[i + 1], wineList[i] + wineList[i + 2],wineList[i + 1]+ wineList[i + 2]))

print(wineList)
