m, n, x, y = map(int, input().split())
#m : 가로, n : 세로, x : 가로, y : 세로
farm = []
max_list = []
max_num = 0

for i in range(n) :
    farm.append(list(map(int, input().split())))

for i in range(n) :
    for j in range(m) :

        if i <= n - y and j <= m - x :

            for a in range(y) :
                for b in range(x) :
                    max_num += farm[i + a][j + b]
        
            max_list.append(max_num)
            max_num = 0

max_list.sort(reverse=True)

print(max_list[0])
