n = int(input())
roadLength = list(map(int, input().split()))
oilPrice = list(map(int, input().split()))
cnt = len(roadLength)
result = 0

mostCheap = min(oilPrice)
i = 0

for oil in oilPrice:
    if oil == mostCheap:
        result += oil * cnt
        break

    else:
        result += oil * roadLength[i]
        i += 1
        cnt -= 1

print(result)
