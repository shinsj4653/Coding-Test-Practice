n = int(input())
triangle = []

for i in range(n):
    triangle.append(list(map(int, input().split())))
    
print(triangle)

for i in range(1, n):

    # if i == 1:
    #     for j in range(2):
    #         triangle[i][j] += triangle[0]

    else:
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
if n > 0:
    print(max(triangle[n - 1]))
else:
    print(triangle[0])
