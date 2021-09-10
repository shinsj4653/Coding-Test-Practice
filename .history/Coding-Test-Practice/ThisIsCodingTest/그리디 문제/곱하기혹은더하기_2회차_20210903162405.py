s = input();
result = 0
#result 에 처음 원소 미리 넣고 시작하기!
#그러면 나머지 1부터 맨 끝 수까지만 확인하면 됨.


for i in range(len(s) - 1) :
    if i == 0:# 처음일때,
        if s[i] == '0' or s[i] == '1' or s[i + 1] == '0' or s[i + 1] == '1' :
            #이것보단 num = int(s[i]) 하고, num이 <= 1 이렇게 하는게 더 깔끔!
            result += int(s[i]) + int(s[i + 1])
        
        else:
            result += int(s[i]) * int(s[i + 1])
        
    else : #나머지일때,
        if s[i + 1] == '0' or s[i + 1] == '1':
            result += int(s[i + 1])
            
        else :
            result *= int(s[i + 1])
            
print(result)