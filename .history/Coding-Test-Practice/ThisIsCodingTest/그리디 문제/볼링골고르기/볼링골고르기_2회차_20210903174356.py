n, m = map(int, input().split())
ball = list(map(int, input().split()))
# 공마다 각 번호 주어지면, 무게다를시, 1번 2번 이랑 2번 1번은 다른 경우아닌가??
# ->

ball.sort()

index = 0
result = 0

for i in range(len(ball) - 1):
    target = ball[i]
    index = i + 1

    while True:
        if target < ball[index] or index == len(ball) - 1:
            break
        index += 1

    if ball[index] <= target:
        break

    else:
        result += len(ball) - index

print(result)
