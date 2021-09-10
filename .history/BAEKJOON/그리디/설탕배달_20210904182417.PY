n = int(input())
result = 0

if n == 3:
    result = 1

elif 0 < n < 5 and n != 3:
    result = -1

while True:
    if (n % 5) % 3 == 0:  # 5로 나눈 나머지가 3의 배수 일때
        result = n // 5 + (n % 5) // 3
        break

    else:  # 아닐떄
        if n > 5:
            n -= 5
            result += 1

        else:  # 5씩 빼다가 결국 중간에 3의 배수인 수가 나오지 않으면, 처음의 수를 3으로 한게 정답.
            result = n // 3

    if n % 3 == 0:
        result += n // 3
        break

print(result)
