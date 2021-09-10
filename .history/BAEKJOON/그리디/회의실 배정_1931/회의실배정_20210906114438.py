n = int(input())
meeting = 0
meetingList = []
result = []

for i in range(n):
    start, end = map(int, input().split())
    # time = end - start  # 시간이 가장 적은 순서대로 정렬
    meetingList.append((start, end))

# meetingList.sort()
# print(meetingList)
result.append(meetingList[0])

for i in range(1, len(meetingList)):
    start, end = result[len(result) - 1]
    currentStart, currentEnd = meetingList[i]
    time = currentEnd - currentStart

    if start < currentStart < end or start < currentEnd < end:
        continue
    elif currentStart <= start and currentStart + time > start:
        continue
    else:
        result.append((currentStart, currentEnd))

print(len(result))
