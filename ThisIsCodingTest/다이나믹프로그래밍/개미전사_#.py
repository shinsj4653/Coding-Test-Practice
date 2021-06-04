#풀긴 풀었지만, 책의 핵심 아이디어 : 보텀업으로, 가장 큰 거 부터 터는 생각X, 첫번째 원소부터 터는 걸 생각

n = int(input())
food = list(map(int, input().split()))
arrived = [False] * len(food)


stolen = 0
i = 0 #현재인덱스

while True:
    count = 0
    
    for status in arrived : 
        if status == False :
            count = 1
    
    if count == 0 :
        break

        
    i = food.index(max(food))
    stolen += food[i]
    food[i] = 0
    arrived[i] = True
    

    
    if i < len(food) - 1 and i > 0 :
        arrived[i + 1] = True
        food[i + 1] = 0

        arrived[i - 1] = True
        food[i - 1] = 0

    elif i == 0 : 
        arrived[i + 1] = True
        food[i + 1] = 0

    elif i == len(food) - 1 :
        arrived[i - 1] = True
        food[i - 1] = 0


print(stolen)

#책의 풀이
n = int(input())

array = list(map(int, input().split()))

d = [0] * 100 #몇번째 원소까지 털었을때를 생각하면, 몇번째 원소에 해당하는 답은 항상 정해져있음.

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n) : 
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])
