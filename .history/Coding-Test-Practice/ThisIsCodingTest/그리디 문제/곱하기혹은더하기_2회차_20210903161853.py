s = input();
result = 0

for i in range(len(s)) :
    if i == 0:# 처음일때,
        if s[i] == '0' or s[i] == '1' or s[i + 1] == '0' or s[i + 1] == '1' :
            result += int(s[i]) + int(s[i + 1])
        
        else:
            result += int(s[i]) * int(s[i + 1])
        
    else : #나머지일때,
        if s[i + 1] == '0' or s[i + 1] == '1':
            result += int(s[i])
            
        else :
            result *= int(s[i])