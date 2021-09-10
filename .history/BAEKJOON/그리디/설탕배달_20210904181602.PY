n = int(input())
result = 0

while True:
    if (n % 5) % 3 == 0:  # 5로 나눈 나머지가 3의 배수 일때
        result = n // 5 + (n % 5) // 3
        break

    else:  # 아닐떄
        if n > 5:
            n -= 5
            result += 1

        else:
            result = n // 3

    if n % 3 == 0:
        result += n // 3

print(result)
