#미해결
n = int(input())
l = []
for i in range(n) :
    math, it = map(int, input().split())
    l.append((math, it))

l = sorted(l, key = lambda x : x[0] reverse = True)

for i in range(len(l)) : 
    print(l.index(l[i]), l[i])

