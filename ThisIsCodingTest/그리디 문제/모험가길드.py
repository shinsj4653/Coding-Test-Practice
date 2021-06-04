n = int(input())
adventure = list(map(int, input().split()))

adventure.sort()

index = 0
total = len(adventure)
group = 0
b = False

while True :
    num = adventure[index]

    total = len(adventure) - index

    for i in range(num) :
        if adventure[index + i] > total :
            b = True
            break
    
    if b == True :
        break
    
    group += 1
    index += num

print(group)

