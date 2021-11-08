n = int(input())
d = [0] * (n + 1)
# d[1] = 1
# d[2] = 2 -> n이 1일때 오류남 : indexerror 주의

# 1 하나 or 0 두 개 붙인

# 선언할때 : d[i for i in range(n + 1)]
# -> 1과 2일 때 1,2 들어가짐
# -> for문 3부터 돌리기 가능해짐

for i in range(n + 1):
    if i == 1:
        d[i] = 1

    elif i == 2:
        d[i] = 2

    else:
        d[i] = (d[i - 1] + d[i - 2]) % 15746

print(d[n])
