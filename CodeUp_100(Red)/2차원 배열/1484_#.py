# n, m = map(int, input().split())
# snail = [[0] * m for _ in range(n)]
# # n : 행, m : 열
# num = 1
# i = 0 #행 
# j = 0 #열

# while num <= n * m : 
    
#     snail[i][j] = num
#     num +=1
    
#     if i == 0 or num > n + m + n:
#         j += 1
#     elif num > m 
#         i -= 1
#     elif num > n + m 
#         j -= 1
#     elif num > m + n + m
#         i += 1


#밑에 정답

n, m = map(int, input().split())
#n : 행, m : 열
a = [[0] * 100 for _ in range(100)]
i = 0
j = 0
direct = 0 #방향 변수 따로 설정

for k in range(1, n * m + 1) :
    a[i][j] = k

    if direct == 0 :
        j += 1#오른쪽
        if j % m == m - 1 and a[i][j] == 0 :
            direct += 1
            if j == m :
                i += 1
                j -= 1

        elif a[i][j] != 0 :
            direct += 1
            i += 1
            j -= 1


    elif direct == 1 :
        i += 1#아래쪽
        if i % n == n - 1 and a[i][j] == 0 :
            direct += 1
        elif a[i][j] != 0 :
            direct += 1
            j -= 1
            i -= 1

    elif direct == 2 :
        j -= 1#왼쪽
        if j == 0 and a[i][j] == 0:
            direct += 1
        elif a[i][j] != 0:
            direct += 1
            j += 1
            i -= 1

    elif direct == 3 :
        i -= 1#위
        if i == 0 and a[i][j] == 0:
            direct = 0 

        elif a[i][j] != 0 :
            i += 1
            j += 1
            direct = 0

for i in range(n) :
    for j in range(m) :
        print(a[i][j], end = " ")
    print()
    