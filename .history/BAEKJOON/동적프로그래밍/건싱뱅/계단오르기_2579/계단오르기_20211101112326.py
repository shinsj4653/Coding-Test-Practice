n = int(input())
stair = []
score = 0
for i in range(6) :
    stair.append(int(input()))
    
d = [0]
d.append(stair[0])

if n > 1 :
    d.append(stair[0] + stair[1])

for i in range(3, n + 1) :
    