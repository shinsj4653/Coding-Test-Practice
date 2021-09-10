#0에서 1로 바뀔때랑 1에서 0으로 바뀔 때의 변수가 둘 다 true일때 뒤집기 발동!

s = input()
zero_to_one = False
one_to_zero = False
result = 0

for i in range(len(s) - 1) :
    if s[i] != s[i + 1] :
        if s[i] == '0' :
            zero_to_one = True
            
        else :
            one_to_zero = True
            
    if zero_to_one == True and one_to_zero == True :
        result += 1
        zero_to_one = False
        one_to_zero = False