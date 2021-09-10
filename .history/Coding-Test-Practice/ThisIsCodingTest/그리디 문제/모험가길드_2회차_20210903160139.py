n = int(input())
fear = list(map(int, input().split()))

fear.sort()
index = 0
count = len(fear) # 배열 안 현재 개수
result = 0

while index < len(fear) :
    f = fear[index];
    if f <= count :
        result += 1
        index += f
        count -= f

print(result)