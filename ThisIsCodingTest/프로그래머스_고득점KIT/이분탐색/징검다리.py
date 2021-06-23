def solution(distance, rocks, n):
    
    INF = 1e9
    
    answer = 0 
    rocks.sort()
    rocks.append(distance)
    
    left, right = 0, distance
    
    while left <= right :
        
        #나는 거리의 최솟값을 mid로 잡음. rock사이 거리가 mid이하면 삭제
        
        mid = (left + right) // 2
        min_distance = INF
        current = 0 
        remove_cnt = 0
        
        for rock in rocks :
            diff = rock - current
            
            if diff < mid :
                remove_cnt += 1
                
            else :
                current = rock
                min_distance = min(min_distance, diff)
                
        if remove_cnt > n :
            #바위를 n보다 많이 제거하면 안됨 : mid줄여서 바위를 조금만 제거
            right = mid - 1
        
        else :
            answer = min_distance
            left = mid + 1
    
    return answer