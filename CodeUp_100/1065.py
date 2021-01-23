a, b, c = input().split()
l = []
n1 = int(a)
n2 = int(b)
n3 = int(c)
l.append(n1)
l.append(n2)
l.append(n3)

for i in l : 
    if i % 2 == 0 :
        print(i)
    