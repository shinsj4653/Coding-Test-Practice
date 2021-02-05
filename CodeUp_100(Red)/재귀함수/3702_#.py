# r, c = map(int, input().split())

# pascal = [[0] * 50 for _ in range(50)]

# x = r - 1
# y = c - 1

# for i in range(50) :
#     for j in range(50) :
#         if i == 0 or j == 0 :
#             pascal[i][j] = 1

# for i in range(1, 50) :
#     for j in range(1, 50) :     
#         pascal[i][j] = pascal[i - 1][j] + pascal[i][j - 1]

#print(pascal[x][y])

#회전 변환된 파스칼 삼각형 말고, 그냥 파스칼 삼각형 구현

pascal = [[[1] for _ in range(i)] for i in range(1, 51)] # 각 행 마다 열 개수가 다르므로

for i in range(2, 50) :
    for j in range(1, i) :
        pascal[i][j] = pascal[i - 1][j] + pascal[i][j - 1]

r, c = map(int, input().split())
print(pascal[r - 1][c - 1])



