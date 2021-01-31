N = int(input())
l = list(map(int, input().split()))
l.sort(reverse = True)
for i in range(N) :
    print(l[i], end = " ")