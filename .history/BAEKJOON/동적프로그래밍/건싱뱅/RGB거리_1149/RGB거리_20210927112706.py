n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

colorStart = cost[0].index(min(cost[0]))
#resultStart = 0 
resultStart += cost[0][colorStart]

colorLast = cost[n - 1].index(min(cost[n - 1]))
#resultLast = 0
resultLast += cost[n - 1][colorLast]

for i in range(1, n) :
    if color == 0 :
        
    elif color == 1 :
        
    elif color == 2 :
        
