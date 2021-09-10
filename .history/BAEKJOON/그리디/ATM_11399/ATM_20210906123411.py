n = int(input())
time = list(map(int, input().split()))
value = 0
result = []

time.sort()
for t in time:
    value += t
    result.append(value)

print(sum(result))
