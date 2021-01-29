import sys

l = list(map(int, input().split()))
for i in l :
    if i % 5 == 0 :
        print(i)
        sys.exit()


print(0)