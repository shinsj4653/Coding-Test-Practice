n = int(input())
d = [0] * 9  # 0 ~ 9
for i in range(0, 9) :
    if i == 0 :
        d[i] = 1
    else :
        

if n == 1:
    print(d[n])
else:

    for i in range(2, n + 1):
        d[i] = (2 ** (i - 1)) * 8 + 1

    print(d[n])
