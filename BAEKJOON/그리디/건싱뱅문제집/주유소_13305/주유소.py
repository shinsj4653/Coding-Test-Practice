INF = 1e9
n = int(input())

roadLength = list(map(int, input().split()))
oilPrice = list(map(int, input().split()))
# cnt = len(roadLength)
result = 0

mostCheap = oilPrice[0]
# road = 0

# for i in range(len(roadLength)):
#     if oilPrice[i] == mostCheap:
#         result += oilPrice[i] * sum(roadLength[i:])
#         break

#     else:
#         result += oilPrice[i] * roadLength[road]
#         road += 1

# 위의 방법 -> 도시별로 지나갈때마다 최솟 값 발견되면 그때그때마다
# 갱신해야하는데, 위의 방법은 최솟값 발견안되면
# 각 도시 기름값을 계속 사용하게 됨.

for i in range(len(roadLength)):

    if oilPrice[i] < mostCheap:
        mostCheap = oilPrice[i]
        result += roadLength[i] * mostCheap

    else:
        result += roadLength[i] * mostCheap

print(result)
