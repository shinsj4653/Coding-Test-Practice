#개수가 더 적은걸 기준으로 ? 그러면 나중에 개수가 적은 수가 연속성을 못 띠면 못 뒤집는데..

string_s = input()
zero_count = 0
one_count = 0

all_same = False

while all_same == False :

    for s in string_s :
        if s == 0 :
            zero_count += 1
    
        elif s == 1 :
            one_count += 1

    if zero_count == len(string_s) or one_count = len(string_s) :
        all_same = True
        continue

    else :
        
        for i in range(len(string_s)) :
            string_s[i] 

    
