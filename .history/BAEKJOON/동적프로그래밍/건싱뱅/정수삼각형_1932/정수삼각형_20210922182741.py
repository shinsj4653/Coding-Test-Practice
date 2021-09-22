n = int(input())
triangle = []
d = [0] * n  # 각 층의 최댓값

for i in range(n):
    if i == 0:
        triangle.append(int(input()))

    else:
        triangle.append(list(map(int, input().split())))

print(triangle)
