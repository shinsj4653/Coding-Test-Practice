n = int(input())
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

startIndex = cost[0].index(min(cost[0]))

for i in range(n) : 
    
