x, y, w, s = map(int, input().split())
x, y = min(x, y), max(x, y)
result = 0

if w * 2 <= s:
    result = x * w + y * w

else:  # 대각선 시간이 더 적을 때
    # if x > y:
    #     result = y * s + (x - y) * w

    # else:
    #     result = x * s + (y - x) * w

    # 왜 아니지?? -> w*2 가 s보다 큰 경우에서, w 혼자 s보다 큰지, 아니면 w만 있을떄는 s보다 작은지를 생각해야!

    if s <= w:  # w혼자서도 s보다 클때
        m = (x + y) % 2
        result = (y - m) * s + m * w
        # 이 부분 이해불가...
        #

    else:  # w혼자서는 s보다 작을 때만 내가 원래 생각한 방법이 적용됨.
        result = x * s + (y - x) * w


print(result)
