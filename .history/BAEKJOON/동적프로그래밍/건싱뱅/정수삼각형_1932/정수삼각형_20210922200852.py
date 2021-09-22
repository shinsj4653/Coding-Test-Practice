n = int(input())
triangle = []
# d = [0] * n  # 각 층의 최댓값

for i in range(n):
    if i == 0:
        triangle.append(int(input()))

    else:
        triangle.append(list(map(int, input().split())))

print(triangle[0])


for i in range(1, n):

    if i == 1:
        for j in range(2):
            triangle[i][j] += triangle[0]

    else:
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

print(max(triangle[n]))
