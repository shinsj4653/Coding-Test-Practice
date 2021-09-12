def solution(n):
    num = n
    result = 0

    if num == 3:
        result = 1
        return result

    elif 0 < num < 5 and num != 3:
        result = -1
        return result

    while True:
        if (num % 5) % 3 == 0:  # 5로 나눈 나머지가 3의 배수 일때
            result = num // 5 + (num % 5) // 3
            return result

        else:  # 아닐떄
            if num > 5:
                num -= 5
                result += 1

            else:  # 5씩 빼다가 결국 중간에 3의 배수인 수가 나오지 않으면, 처음의 수를 3으로 한게 정답.
                result = n // 3
                return result

        if num % 3 == 0:
            result += num // 3
            return result


print(solution(int(input())))
