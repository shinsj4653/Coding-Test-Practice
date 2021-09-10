n = int(input())
time = list(map(int, input().split()))
value = 0
result = 0

time.sort()
for t in time:
    value += t
    result += value
    
# 2번째 방법  
# for t in time:
#     result += t * n
#     n -= 1

print(result)
