x, y, w, s = map(int, input().split())
result = 0

if w * 2 <= s:
    result = x * w + y * w

else:  # 대각선 시간이 더 적을 때
    # 왜 아니지?? -> w*2 가 s보다 큰 경우에서, w 혼자 s보다 큰지, 아니면 w만 있을떄는 s보다 작은지를 생각해야!
    if x > y:
        result = y * s + (x - y) * w

    else:
        result = x * s + (y - x) * w

print(result)
