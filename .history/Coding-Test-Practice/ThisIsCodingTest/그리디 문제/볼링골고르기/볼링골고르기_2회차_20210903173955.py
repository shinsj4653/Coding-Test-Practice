n, m = map(int, input().split())
ball = list(map(int, input().split()))

ball.sort()

index = 0
result = 0

for i in range(len(ball) - 1):
    target = ball[i]
    index = i + 1

    while True:
        if target < ball[index]:
            break
        index += 1

    result += len(ball) - index

print(result)
