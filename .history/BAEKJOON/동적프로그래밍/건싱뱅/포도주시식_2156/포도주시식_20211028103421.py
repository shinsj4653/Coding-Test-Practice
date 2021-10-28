n = int(input())
wine = []
startFirst = []
startSecond = []
startThird = []

for i in range(n):
    wine.append(int(input()))
print(wine)

# 연속 3개 불가
# 연속 2개까지는 가능
# n n + 1 , 모두 마시기 아니었으면 개 어려웠을듯
