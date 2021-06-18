#스택 원리를 이용한 풀이
#time변수 활용!

def solution(progresses, speeds) :
    answer = []
    time = 0
    count = 0
    
    while len(progresses) > 0 :
        
        if progresses[0] + time * speeds[0] >= 100 :
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else :
            if count > 0 :
                answer.append(count)
                count = 0
            
            time += 1

    answer.append(count)
    return answer
    
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))