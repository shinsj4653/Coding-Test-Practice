total = 0
r, g, b = map(int, input().split())
for i in range(r) :
    for j in range(g) :
        for k in range(b) :
            print(i,j,k)
            k+=1
            total+=1
        j+=1
    i+=1
print(total)