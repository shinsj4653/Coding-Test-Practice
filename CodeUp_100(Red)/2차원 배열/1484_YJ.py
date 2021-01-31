global a,b
sn = []
sm = 0
a, b = map(int,input().split())
sn = [[0] * b for _ in range(a)]
def snale(z,x,c,k):
    global sm
    if sm==a*b:
        return k
    if x-1==c and z-1==c:
        sm+=1
        k[c][c]=sm
        return k
    for i in range(c,x-1):
        sm+=1
        k[c][i]=sm
        if sm==a*b:
            return k
    for i in range(c,z-1):
        sm+=1
        k[i][x-1]=sm
        if sm==a*b:
            return k
    for i in range(x-1,c,-1):
        sm+=1
        k[z-1][i]=sm
        if sm==a*b:
            return k
    for i in range(z-1,c,-1):
        sm+=1
        k[i][c]=sm
        if sm==a*b:
            return k
    return snale(z-1,x-1,c+1,k)
    
sn = snale(a,b,0,sn)

for i in range(a):
    for j in range(b):
        print(sn[i][j],end=" ")
    print()
