#접근 조차 못함...
def solution(number, k):
    answer = ''
    
    #stack에 입력값을 순서대로 삽입
    stack = [number[0]]
    
    for num in number[1:] :
    #들어오는 값이 stack보다 크면, 기존의 값 제거하고 새로운 값으로 바꿈. 
    
        while len(stack) > 0 and stack[-1] < num and k > 0 :
        
            k -= 1
        
            stack.pop()
    
        stack.append(num)
    
    #만약 충분히 제거 못했으면, 남은 부분은 삭제
    #이미 큰수부터 앞에서 채워넣었기 때문에 남은 부분은 필요x
    if k != 0 :
        stack = stack[:-k]
        #0, 즉 첨부터 -k면 끝에서부터 카운트한 자릿수 직전까지
        
    return  ''.join(stack)