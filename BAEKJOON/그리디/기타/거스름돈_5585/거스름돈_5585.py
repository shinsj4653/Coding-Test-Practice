n = int(input())
change = 1000 - n
result = 0
coin = [500, 100, 50, 10, 5, 1]

for c in coin:
    if change >= c:  # -> 왜 이 기준 넣으면 틀릴까??
        # change == c 인 경우도 포함시켜야한다.
        result += change // c
        change %= c

print(result)
