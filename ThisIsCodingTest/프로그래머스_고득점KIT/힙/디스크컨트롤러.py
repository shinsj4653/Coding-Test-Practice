# import heapq

# def solution(jobs):
#     answer = 0
#     ans = []
#     q = []
    
#     for i in jobs :
#         heapq.heappush(q, (i[1], i[0]))#앞이 시간, 뒤가 시점
        
#     while q :
        
#         t = heapq.heappop(q)
        
#         ans.append((sum(ans) + t[0] - t[1]))
            
#     answer = int(sum(ans) / len(ans)) 
            
#     return answer

#아무리 생각해도..왜 틀렸는지 모르겠..

#안 풀리면 문제 조건들을 다시 생각 -> 작업 수행하고 있지 않을때에는 먼저 요청이 들어온 작업부터 처리

import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    h = []
    
    while i < len(jobs) :
        
        for j in jobs :
            if start < j[0] <= now : #이걸 생각해내는게 핵심!
                heapq.heappush(h, (j[1], j[0]))
                
        if len(h) > 0 :
            current = heapq.heappop(h)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        
        else : #현재 들어온 요청이 없을때 : 시간을 계속 흐르게 해줘야.
            now += 1
            
    return int(answer / len(jobs))

#현재시점에서 처리할 수 있는 작업인지를 판별하는 조건
#-> 작업의 요청시간이 바로 이전에 완료한 작업의 시작시간보다 크고, 현재 시점보다 작거나 같아야함.
print(solution([[0, 3], [1, 9], [2, 6]]))