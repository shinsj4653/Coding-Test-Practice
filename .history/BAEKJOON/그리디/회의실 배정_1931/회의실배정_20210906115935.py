n = int(input())
meeting = 0
meetingList = []
result = []

for i in range(n):
    start, end = map(int, input().split())
    # time = end - start  # 시간이 가장 적은 순서대로 정렬
    meetingList.append((start, end))

meetingList.sort(key=lambda x: x[1])
print(meetingList)

# for i in range(1, len(meetingList)):
#     start, end = result[len(result) - 1]
#     currentStart, currentEnd = meetingList[i]
#     time = currentEnd - currentStart

#     if start < currentStart < end or start < currentEnd < end:
#         continue
#     elif currentStart <= bigStart and currentEnd > bigStart:
#         continue
#     else:
#         result.append((currentStart, currentEnd))

#     if currentStart < bigStart:
#         bigStart = currentStart

#     if bigEnd < currentEnd:
#         bigEnd = currentEnd

# print(len(result))
