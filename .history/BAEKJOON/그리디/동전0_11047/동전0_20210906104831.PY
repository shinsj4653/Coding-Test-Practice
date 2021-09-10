n, k = map(int, input().split())
result = 0
coin = []

for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)
