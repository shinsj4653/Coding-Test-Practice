n = int(input())
paper = []
countZero = 0
countOne = 0
countMinus = 0

for i in range(n):
    paper.append(list(map(int, input().split())))
x = 0
y = 0


def countSum(x, y, n):
    sum = 0
    for x in range(x, x + n):
        for y in range(y, y + n):
            sum += paper[x][y]

    if sum == 0:
        return 0

    elif sum == n * n:
        return 1

    elif sum = -(n * n) :
        return -1


while True:
    num = countSum(x, y, n)

    if num == 0:
        countZero += 1

    elif num == 1:
        countOne += 1
        
    else 

print(countZero)
print(countOne)
print(countMinus)
