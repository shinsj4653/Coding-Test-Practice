n = int(input())
time = list(map(int, input().split()))
result = 0

time.sort()
for t in time:
    result += result + time

print(time)
