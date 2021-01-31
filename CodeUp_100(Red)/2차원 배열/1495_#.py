#2차원 구간합 구하기
#S(i, j)는 a(1, 1) 과 a(i, j)를 양 대각 끝 꼭지점으로 하는 직사각형 범위 면적 안의 모든 a 원소의 합
#Row 방향으로 한번 1차원 구간합을 모두 구한 뒤, Col 방향으로 구해진 구간합을 다시 구간합 하면된다.

#자신의 왼쪽과 위를 더한 거에 i - 1 , j - 1을 빼면 중복된 부분이 제거됨.

#시간 단축위해 조건문 사용!

n, m, k = map(int, input().split()) #n : 행, m : 열, k : 데이터 개수
d = [[0] * 1000 for _ in range(1000)]
d_sum = [[0] * m for _ in range(n)]
for i in range(k) :
    x1, y1, x2, y2, u = map(int, input().split())
    d[x1][y1] += u
    d[x2 + 1][y2 + 1] += u
    d[x1][y2 + 1] -= u
    d[x2 + 1][y1] -= u

for i in range(n) :
    for j in range(m) :
        print(d[i][j], end = " ")
    print()

# sum = 0
# #구간합 시작
# for i in range(n) :
#     for j in range(m) :
        
#         for a in range(i + 1) :
#             for b in range(j + 1) :
#                 sum += d[a][b]

#         d_sum[i][j] = sum
#         sum = 0
# print()

# for i in range(n) :
#     for j in range(m) :
#         print(d_sum[i][j], end = " ")
#     print()
#정답참고
#원래 배열에서 계속해서 누적합들을 구해가면서 원래값에 덮어씌우면서 진행
for i in range(n) :
    for j in range(m) :
        if not(i) and not(j) :
            d_sum[i][j] = d[i][j]
        elif not(i) :
            d_sum[i][j] = d_sum[i][j - 1] + d[i][j]
        elif not(j) :
            d_sum[i][j] = d_sum[i - 1][j] + d[i][j]
        else :
            d_sum[i][j] = d_sum[i - 1][j] + d_sum[i][j - 1] + d[i][j] - d_sum[i - 1][j - 1]

        print(d_sum[i][j], end = " ")
    print()