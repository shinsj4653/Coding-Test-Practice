# 연속 3개 불가
# 연속 2개까지는 가능
# n n + 1 , 모두 마시기 아니었으면 개 어려웠을듯

n = int(input())
wineList = []
startFirst = []
startSecond = []
startThird = []

sumFirstSec = 0
sumSecThird = 0
sumFirstThird = 0

for i in range(n):
    wine = int(input())
    wineList.append(wine)
    if i % 3 == 1:
        startFirst.append(wine)

    elif i % 3 == 2:
        startSecond.append(wine)

    else:
        startThird.append(wine)
# print(startFirst)
# print(startSecond)
# print(startThird)

sumFirstSec = sum(startFirst) + sum(startSecond)
sumFirstThird = sum(startFirst) + sum(startThird)
sumSecThird = sum(startSecond) + sum(startThird)


# 연속 3개 불가
# 연속 2개까지는 가능
# n n + 1 , 모두 마시기 아니었으면 개 어려웠을듯
