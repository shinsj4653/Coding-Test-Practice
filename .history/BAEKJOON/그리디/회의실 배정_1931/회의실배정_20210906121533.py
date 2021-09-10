n = int(input())
meeting = 0
meetingList = []
result = 1

for i in range(n):
    start, end = map(int, input().split())
    # time = end - start  # 시간이 가장 적은 순서대로 정렬
    meetingList.append((start, end))

meetingList.sort(key=lambda x: x[1])
# print(meetingList)
bigEnd = meetingList[0][1]

for i in range(1, len(meetingList)):
    if bigEnd <= meetingList[i][0]:
        bigEnd = meetingList[i][1]

    result += 1
print(result)
