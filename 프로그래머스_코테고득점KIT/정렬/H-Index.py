#미해결
#citation 요소 중 하나가 답이 아님!
#비교하다가 인덱스에 해당하는 배열값이 인덱스보다 작거나 같으면 해당 인덱스가 정답
#규칙 찾는 것도 하나의 방법

def solution(citations):
    
    citations.sort(reverse = True)
    answer = 0
    
    for i in range(len(citations)) :
        
        if citations[i] <= i :
            answer = i
            break
            
    
            
    return answer

print(solution([3, 0, 6, 1, 5]))