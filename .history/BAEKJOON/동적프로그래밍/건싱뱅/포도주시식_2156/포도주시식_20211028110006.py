# 연속 3개 불가
# 연속 2개까지는 가능
# n n + 1 , 모두 마시기 아니었으면 개 어려웠을듯

# 첫 시도 -----------------------------------

# n = int(input())
# wineList = []
# startFirst = []
# startSecond = []
# startThird = []

# sumFirstSec = 0
# sumSecThird = 0
# sumFirstThird = 0

# for i in range(n):
#     wine = int(input())
#     wineList.append(wine)
#     if i % 3 == 0:
#         startFirst.append(wine)

#     elif i % 3 == 1:
#         startSecond.append(wine)

#     elif i % 3 == 2:
#         startThird.append(wine)
# # print(startFirst)
# # print(startSecond)
# # print(startThird)

# sumFirstSec = sum(startFirst) + sum(startSecond)
# sumFirstThird = sum(startFirst) + sum(startThird)
# sumSecThird = sum(startSecond) + sum(startThird)

# sumList = []
# sumList.append(sumFirstSec)
# sumList.append(sumFirstThird)
# sumList.append(sumSecThird)

# print(max(sumList))


# 두번째 시도

n = int(input())
wineList = []
startFirst = []
startSecond = []
startThird = []

sumFirstOne = 0 #1, 2 / 1, 2
sumFirstTwo = 0 # 2, 1/ 2, 1
sumSecondOne = 0 #1, 2/1, 2

for i in range(n):
    wine = int(input())
    wineList.append(wine)
    if i == 0 :
        
