x, y, w, s = map(int, input().split())
result = 0

if w * 2 <= s:
    result = x * w + y * w

else:  # 대각선 시간이 더 적을 때
    if x > y:
        result = y * s + x * w

    else:
        result = x * s + y * w

print(result)
