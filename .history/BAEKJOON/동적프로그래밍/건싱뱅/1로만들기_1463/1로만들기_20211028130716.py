x = int(input())
result = 0

while x > 1:

    if x % 3 == 0:
        x //= 3

    elif x % 2 == 0:
        x //= 2

    else:
        x -= 1

    result += 1
    if x == 1:
        break
print(result)
