# 처음 아이디이 : 웅덩이가 겹쳐지는 상황까지 포함하여 총 웅덩이의 길이를 구해서 마지막에 l 로 나눴음.
# -> 그럴 필요 없이, 그냥 좌표만 고려하면 됨. 어차피 다 덮기만 하면 되니까.
# 정답 아이디어 : 매 좌표마다 판자 설치하는 위치를 업데이트 하며, 끝 좌표를 넘어가기 전까지 계속 깔음.
import heapq

n, l = map(int, input().split())
q = []
result = 0

for i in range(n):
    start, end = map(int, input().split())
    heapq.heappush(q, (start, end))

q.sort(key=lambda x: x[0])

upcnt = 0
for i in range(0, len(q)):
    if q[i][0] > upcnt:  # 이전 판자 위치보다 시작 좌표가 크면, 시작좌표로 위치 업데이트
        # 시작좌표가 작으면, 위치 업데이트 필요x -> 판자가 이미 시작좌표는 덮고 있음.
        upcnt = q[i][0]

    while upcnt < q[i][1]:  # 끝좌표보다 작으면, 계속 판자 깔아야함.
        upcnt += l
        result += 1

print(result)
