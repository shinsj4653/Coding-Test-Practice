#회전 변환된 파스칼 삼각형 말고, 그냥 파스칼 삼각형 구현 
#r, c = map(int, input().split())

# pascal = [[1 for _ in range(i)] for i in range(1, 51)] # 각 행 마다 열 개수가 다르므로

# for i in range(2, 50) :
#     for j in range(1, i) : -> j를 1부터 i값 까지.
#         pascal[i][j] = pascal[i - 1][j] + pascal[i][j - 1]


# print(pascal[r - 1][c - 1])

#회전 변환된 파스칼 삼각형
r, c = map(int, input().split())
pascal = [[1] * 50 for _ in range(50)]
x = r - 1
y = c - 1

for i in range(1, 50) :
    for j in range(1, 50) :
        pascal[i][j] = pascal[i - 1][j] + pascal[i][j - 1]
    
print(pascal[x][y] % 100000000)