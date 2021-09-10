#문제 내용을 이진탐색화를 어떻게 해야할지 모르겠음..
#인터넷풀이
#핵심 : 최소, 최대 범위를 구한 뒤, 구하려고 하는 답을 범위를 좁혀가며 찾음.

def solution(n, times) :
    answer = 0 
    left = 1
    right = n * max(times) #최대 범위
    while left <= right :
        
        mid = (left + right) // 2
        
        count = 0 
        for time in times :
            count += mid // time
            #심사 인원수를 넘으면 다음 단계
            if count >= n : break
            

        #n명을 심사할 수 있는 경우
        #한 심사관에게 주어진 시간을 줄여본다.
        
        if count >= n :
            answer = mid
            right = mid - 1
            
        else :
            left = mid + 1
            
    return answer
