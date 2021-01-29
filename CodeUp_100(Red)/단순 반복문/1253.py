a, b = map(int, input().split())
l = []
if a > b :

    for i in range(a - b + 1) :
        l.append(i + b)


else :

    for i in range(b - a + 1) :
        l.append(i + a)

for j in l :
    print(j,end = " ")

