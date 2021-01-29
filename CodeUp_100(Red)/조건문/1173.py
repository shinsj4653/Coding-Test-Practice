h, m = map(int, input().split())
if m >= 30 :
    print(h,m - 30)
elif h == 0 : 
    print(23,m + 30)
else : 
    print(h - 1,m + 30)