w, h, b = map(int, input().split())
ans = (w * h * b) / (8 * 1024 * 1024)
print(format(ans, ".2f"),"MB")