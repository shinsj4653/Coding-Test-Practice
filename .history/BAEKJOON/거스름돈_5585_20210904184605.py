n = int(input())
change = 1000 - n
result = 0
coin = [500, 100, 50, 10, 5, 1]

for c in coin:
    if change > c:
        result += change // c
        change %= c

print(result)
