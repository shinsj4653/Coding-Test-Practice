#런타임 에러..어떡하지..
#max_q , min_q 따로 만들지 않고 최댓값 뽑을땐 .pop(-1) 끝에 있는거 뽑기 사용!

import heapq

def solution(operations):
    answer = []
    op = []
    
    #최댓값 저장용 큐, 최솟값 저장용 큐 따로 저장.
    #max_q = []
    min_q = []
    
    i_count = 0
    d_count = 0
    
    for o in operations :
        
        op.append(o.split())
            
    for i in op :
        
        if i[0] == 'I' :
            heapq.heappush(min_q, int(i[1]))
            #heapq.heappush(max_q, (-int(i[1]), int(i[1])))
            i_count += 1 
            
        elif i[0] == 'D' :
            d_count += 1
            
            if len(min_q) > 0 :#q안이 비어있으면 pop연산 하면 안됨!
                if i[1] == '-1' :
                    heapq.heappop(min_q)
                
            
                elif i[1] == '1' :
                    min_q.pop(-1)
                           
    
    if d_count >= i_count :
        return [0, 0]
    
    else :
        
        answer.append(max(min_q)) 
        answer.append(min(min_q))
        
        #pop으로 안하고 max, min으로 하는이유
        #하나만 남아 있을 경우르 대비해서.
    
    
    return answer
#또다른 풀이
#for문 안에서 I 인지 D인지 본다음에, 바로 처리.
import heapq

def solution(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split(' ')
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]