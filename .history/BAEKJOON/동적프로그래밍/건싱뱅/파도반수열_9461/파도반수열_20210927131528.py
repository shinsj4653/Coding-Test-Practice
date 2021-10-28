n = int(input())
numList = []
d = [0] * 101
for i in range(n):
    numList.append(int(input()))

d[1] = 1
d[2] = 1
d[3] = 1

for num in numList:
    for i in range(4, num + 1):
        if d[i] :
            break   
        else :
            d[i] = d[i - 3] + d[i - 2]
    print(d[num])
