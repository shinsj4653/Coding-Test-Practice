t = int(input())
result = []
fold_list = []
for i in range(t):
    fold = input()
    fold_list.append(fold)

# 1이랑 0변할때를 활용 -> 문자열뒤집기랑 비슷??
# 3개씩 기준으로 1 00 혹은 0 11 형태여야함!
for f in fold_list:
    cnt = 0
    while cnt < len(f) // 3:
        if f[3 * cnt : 3 * cnt + 3] != "100" or f[3 * cnt : 3 * cnt + 3] != "011":
            result.append("NO")
            break
        cnt += 1
    else:
        result.append("YES")

for r in result:
    print(r)
