#문제 제발 잘 읽기!
#보트는 최대 "2명" 타기가능!!!!!!!!!!!!!!!


from collections import deque
import heapq

#보트의 최소 개수 : 큰 무게부터 고려하면서!

def solution(people, limit):
    
    answer = 0
    
    people.sort(reverse=True)
    
    heapq.heapify(people)
    #print(people)
    
    
    st = []
    
    st.append(heapq.heappop(people))
    
    while people :
        
        if len(st) == 0 :
            heapq.heappush(st, (heapq.heappop(people)))
            heapq.heappush(st, (heapq.heappop(people)))
            
        else :
            heapq.heappush(st, (heapq.heappop(people)))
        
        if st[0] + st[1] <= limit :
            heapq.heappop(st)
            heapq.heappop(st)
            answer += 1 
            
        else :
            heapq.heappop(st)
            answer += 1
    
    if st :
        answer += len(st)
        
                
    return answer

#아무리봐도 내 코드 맞는것 같은데...흠
#인터넷 풀이
#보트의 최소 개수 : 큰 무게부터 고려하면서!

def solution(people, limit):
    
    
    
    #정렬하는 건 맞음
    #다만 주의 : 인덱싱이 아니라 pop 혹은 del remove 등 리스트 자체에서 빼버리면 효율성 부분에서 틀릴수있음.
    
    
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
        
        
    return len(people) - answer