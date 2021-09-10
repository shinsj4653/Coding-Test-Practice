n = int(input())
metting = 0
mettingList = []

for i in range(n):
    start, end = map(int, input().split())
    time = end - start  # 시간이 가장 적은 순서대로 정렬
    mettingList.append((time, start))

mettingList.sort()
print(meetingList)
