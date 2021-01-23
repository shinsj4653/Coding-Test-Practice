#print(int(not(0)))

# baduk = []

# for i in range(19) : 
#     row = list(map(int, input().split()))
#     baduk.append(row)

# n = int(input())

# for i in range(n) :
#     x, y = map(int, input().split())
#     for j in range(19) :
#         [x - 1][j] = int(not([x - 1][j]))
#         [j][y - 1] = int(not([j][y - 1]))

# for i in range(19) : 
#     print(baduk[i])

baduk = []

for i in range(19) : 
    row = list(map(int, input().split()))
    baduk.append(row)

#print(baduk)
#print(baduk[2][2])

n = int(input())

for _ in range(n) :
    x, y = map(int, input().split())
    for j in range(19) :
        baduk[x - 1][j] = int(not(baduk[x - 1][j]))
        baduk[j][y - 1] = int(not(baduk[j][y - 1]))


for i in range(19) : 
    for j in range(19) :
        print(baduk[i][j],end = " ")
    print()

        