n = int(input())
fear = list(map(int, input().split()))

fear.sort(reverse=True)
index = 0
count = len(fear) # 배열 안 현재 개수
result = 0

while index < len(fear) :
    f = fear[index];
    if f <= count :
        result += 1
        index += f
        count -= f
    #이런식으로 index를 계속해서 많이 더하면, 그룹의 개수는 최소가 될 수도 있음...

print(result)