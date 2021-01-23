N = int(input())
l = list(map(int, input().split()))
for i in range(N) :
    print(l[N - 1 - i], end = " ")