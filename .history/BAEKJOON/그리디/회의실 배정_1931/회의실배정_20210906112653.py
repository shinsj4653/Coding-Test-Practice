n = int(input())
meeting = 0
meetingList = []
result = []

for i in range(n):
    start, end = map(int, input().split())
    time = end - start  # 시간이 가장 적은 순서대로 정렬
    meetingList.append((start, end))

meetingList.sort(key=lambda x: x[1] - x[0])
# print(meetingList)
result.append(meetingList[0])

for i in range(1, len(meetingList)):
    start, end = meetingList[i]
    for r in result:
        if r[0] < start < r[1] or r[0] < end < r[1]:
            break

    else:
        result.append((start, end))

print(len(result))
