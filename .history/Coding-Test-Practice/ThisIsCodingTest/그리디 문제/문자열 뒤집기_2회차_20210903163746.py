#0에서 1로 바뀔때랑 1에서 0으로 바뀔 때의 변수가 둘 다 true일때 뒤집기 발동!

s = input()
zero_to_one = false
one_to_zero = false

for i in range(len(s) - 1) :
    if s[i] != s[i + 1] :
        if s[i] == '0' :
            