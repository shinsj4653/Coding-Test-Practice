# from collections import deque #from collections 잊지말기!

# def solution(priorities, location):
#     answer = 0
#     a_list = [] #뽑히는 순서 기록한 리스트
    
#     q = deque()
    
#     for i in range(len(priorities)) :
#         q.append((chr(ord('A') + i), priorities[i]))
    
#     print(q)
    
#     find = chr((ord('A') + location))
    
    
    
    
        
#     while len(q) > 0 :
        
#         max_p = max(priorities)
    
#         for i in range(len(priorities)) :
        
#             p = q[0][1]
#             print(p)
        
#             if p == max_p :
#                 x = q.popleft()
#                 priorities.remove(priorities[priorities.index(p)]) #remove(), index() 함수암기!
#                 a_list.append(x)
#                 break
        
#             for j in range(1, len(priorities)) :
            
#                 if priorities[j] > p :
#                     x = q.popleft()
#                     print(x)
#                     q.append(x)
#                     break
                
    
#     print(q)
    
#     for idx, x in enumerate(a_list) :
#         if x[0] == find :
#             answer = idx + 1
    
    
#     return answer

#왜 위 풀이로 안 풀리지? -> max_num 찾았다고 바로 끝내면 안됨
#뒤에 남은 순서들도 중요도에 따라 정렬해야됨

#priorities 배열 활용하여 정렬하면서, a_list에 기록
#priorities배열에서 가장 큰 원소 빼면서 갱신시켜야 함
#밑 풀이도 참고

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue): #pop 시킨 다음 나머지 원소들 비교할땐 for q in queue 활용
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

print(solution([1, 1, 9, 1, 1, 1], 0))