# a, b = map(int, input().split())
# x, y, z = map(int, input().split())

# g = []

# old_g = [[0] * (b + 2) for _ in range(a + 2)]

# next_g = [[0] * (b + 2) for _ in range(a + 2)]

# for i in range(a) :
#     g.append(list(map(int, input().split())))


# for i in range(a) :
#     for j in range(b) :
#         old_g[i + 1][j + 1] = g[i][j]
        



# k = int(input())

# for _ in range(k) :

#     for i in range(1, a + 1) :
#         for j in range(1, b + 1) :

#             if old_g[i][j] == 0 :
#                 life = 0

#                 for m in range(i - 1 , i + 2) :
#                     for n in range(j - 1, j + 2) :
#                         if m == i and n == j :
#                             continue
#                         else :
#                             if old_g[m][n] == 1 :
#                                 life += 1
#                 if life == x :
#                     next_g[i][j] = 1



#             elif old_g[i][j] == 1 :

#                 life = 0

#                 for m in range(i - 1 , i + 2) :
#                     for n in range(j - 1, j + 2) :
#                         if m == i and n == j :
#                             continue
#                         else :
#                             if old_g[m][n] == 1 :
#                                 life += 1

#                 if life >=y and life < z :
#                     next_g[i][j] = 1

#                 elif life >= z :
#                     next_g[i][j] = 0

#     old_g = next_g

#     next_g = [[0] * (b + 2) for _ in range(a + 2)]

# for i in range(1, a + 1) :
#     for j in range(1, b + 1) :
#         print(old_g[i][j], end = " ")
#     print()

#시간 초과 해결풀이 -> 8구간 모두 탐색대신 합을 이용하여(생명들이 0, 1로 이루어져 있다는 특징 활용)
a, b = map(int, input().split())
x, y, z = map(int, input().split())

g = []

old_g = [[0] * (b + 2) for _ in range(a + 2)]

new_g = [[0] * (b + 2) for _ in range(a + 2)]

for i in range(a) :
    g.append(list(map(int, input().split())))


for i in range(a) :
    for j in range(b) :
        old_g[i + 1][j + 1] = g[i][j]

k = int(input())

while k != 0  :
    for i in range(1, a + 1) :
        for j in range(1, b + 1) :
            new_g[i][j] = old_g[i - 1][j - 1] + old_g[i - 1][j] + old_g[i - 1][j + 1] + old_g[i][j - 1] + old_g[i][j + 1] + old_g[i + 1][j - 1] + old_g[i + 1][j] + old_g[i + 1][j + 1]

            if old_g[i][j] == 0 :
                new_g[i][j] = new_g[i][j] == x and 1 or 0

            else :
                new_g[i][j] = y <= new_g[i][j] < z and 1 or 0
    
    old_g = new_g
    k -= 1

for i in range(1, a + 1) :
    for j in range(1, b + 1) :
        print(old_g[i][j], end = " ")
    print()