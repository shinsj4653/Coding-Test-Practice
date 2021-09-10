def solution(s):
    answer = -1
    
    stack = []

    idx = 0
    
    while True :
        
        stack.append(s[idx])
        #맨 첨에는 스택에 하나밖에 없음..그래서indexerror..
        #if stack[-1] == stack[-2] : 밑에 문구로 고침.
        if len(stack) >= 2 and stack[-1] == stack[-2] :
    
            
            stack.pop()
            stack.pop()
        
        if idx == len(s) - 1 :
            if len(stack) == 0 :
                answer = 1
                break
            
            else :
                answer = 0
                break
        
        idx += 1
    
    return answer

print(solution("baabaa"))