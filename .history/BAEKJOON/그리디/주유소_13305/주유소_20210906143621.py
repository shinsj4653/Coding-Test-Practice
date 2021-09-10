n = int(input())
roadLength = list(map(int, input().split()))
oilPrice = list(map(int, input().split()))
cnt = len(roadLength)
result = 0

mostCheap = min(oilPrice[0 : len(oilPrice) - 1])
road = 0

for i in range(len(oilPrice) - 1):
    if oilPrice[i] == mostCheap:
        result += oilPrice[i] * cnt
        break

    else:
        result += oilPrice[i] * roadLength[road]
        road += 1
        cnt -= 1

print(result)
