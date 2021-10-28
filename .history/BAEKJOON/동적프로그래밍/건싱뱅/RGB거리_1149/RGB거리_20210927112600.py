n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

color = cost[0].index(min(cost[0]))
resultStart = 0 
resultStart += cost[0][color]

for i in range(1, n) :
    if color == 0 :
        
    elif color == 1 :
        
    elif color == 2 :
        
