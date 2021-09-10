n = int(input())
meeting = 0
meetingList = []

for i in range(n):
    start, end = map(int, input().split())
    time = end - start  # 시간이 가장 적은 순서대로 정렬
    meetingList.append((start, time))

meetingList.sort()
print(meetingList)
