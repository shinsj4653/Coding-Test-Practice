# #힙 : 우선순위 큐를 구현하기 위하여 사용하는 자료구조 중 하나
# from collections import deque

# def solution(scoville, K):
    
#     q = deque(scoville)
#     print(q)
    
#     count = 0 
    
#     while scoville :
        
#         num1 = scoville.pop(0)
        
#         if num1 >= K :
#             continue
        
#         else :
            
#             if scoville == False :
#                 count = -1
#                 return count
            
#             else :
#                 num2 = scoville.pop(0)
#                 new_num = num1 + num2 * 2
#                 count += 1
#                 q.appendleft(new_num)  
    
#     return count

# #시간초과문제..
# #해결방법 : heapq사용!

# import heapq #우선순위 큐가 덱보다 빠름 -> 우선순위 큐라 크기 순으로 자동정렬됨.

# def solution(scoville, K):
    
#     heapq.heapify(scoville)
    
#     count = 0

    
    
#     while len(scoville) > 0 :
        
        
#         num1 = heapq.heappop(scoville)
        
#         if num1 >= K :
            
#             if num1 == K and len(scoville) == 0 :
#                 return count
            
#             else :
#                 continue
        
#         else :
            
#             num2 = heapq.heappop(scoville)
#             new_num = num1 + num2 * 2
            
#             if len(scoville) > 0 :
#                 count += 1
#                 heapq.heappush(scoville, new_num)  
                
#             else :#만약 다 비었을때 , 마지막 두 수를 가지고 만든 new_num 확인해서 K 보다 작으면 바로 끝내기! 시간절약할수 있음.
#                 if new_num < K :
#                     return -1
    
    
#     return count

#반례 : 1, 2, 3 -> K : 11 : 딱맞게 하나가 K랑 같게 나오는경우

#근데 자꾸 16번 테케가 오류..
#밑에 인터넷 풀이


import heapq


def solution(scoville, k):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)

    mix_cnt = 0
    while heap[0] < k: #heap[0] , 즉 최솟값이 K 이상이면 더 이상 할 필요 X
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        mix_cnt += 1

    return mix_cnt

print(solution([1, 2, 3, 9, 10, 12], 7))

#프로그래머스 풀이
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0: #다 뽑았는데도 마지막 pop한게 K못넘으면 못 만듬!
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2) #자동적으로 크기정렬됨.
        answer += 1  

    return answer