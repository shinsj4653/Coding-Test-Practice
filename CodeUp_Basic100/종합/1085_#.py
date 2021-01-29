h, b, c, s = map(int, input().split())
ans = (h * b * c * s) / (8 * 1024 * 1024)
print(round(ans, 1),"MB")

# 8bit = 1byte
# 1bit = 1/8 byte
# 따라서, bit에서 byte로 넘어가려면 1/8 을 해줘야함.