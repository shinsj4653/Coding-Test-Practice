# sort를 할 시에 dist에 플러스 -> 각 단계 리스트 개수의 반 값을 한거를 곱합
# 첫 번째 값이 두 번째 값보다 클때만 swap

n = int(input())
cowList = []
dist = 0
plusCount = 1  # 비교하는 간격
startIndex = 0

for i in range(2 ** n):
    cowList.append(int(input()))

for i in range(2 ** n - 1):
    if cowList[startIndex] > cowList[startIndex + plusCount]:
        (
            cowList[startIndex : startIndex + plusCount],
            cowList[startIndex + plusCount : startIndex + plusCount * 2],
        ) = (
            cowList[startIndex + plusCount : startIndex + plusCount * 2],
            cowList[startIndex : startIndex + plusCount],
        )

        dist += plusCount * plusCount * 2

    if startIndex + plusCount * 2 == len(cowList):
        startIndex = 0
        plusCount *= 2

    else:
        startIndex += plusCount * 2


print(dist)
