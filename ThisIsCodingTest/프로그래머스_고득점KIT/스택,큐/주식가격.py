def solution(prices):
    answer = []
    
    while prices :
        p = prices.pop(0)
        count = 0
        
        for flow in prices :
            if p > flow :
                count += 1
                break
            
            else :
                count += 1
        
        answer.append(count)
    
    
    
    return answer

#방법은 맞음..시간초과가 문제..
#해결 방법 : deque()사용
#넣고 빼는 속도가 리스트에 비해 빠름!