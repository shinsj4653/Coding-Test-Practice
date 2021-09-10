n = int(input())
time = list(map(int, input().split()))
value = 0
result = 0

time.sort()
for t in time:
    value += t
    result += value

print(result)
