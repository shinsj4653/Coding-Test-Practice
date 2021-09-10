#해결

def plusorminus(num, index, numbers, target) :
         
        global answer
        if index == len(numbers) and num == target : #len(numbers) - 1하면 맨 끝 수는 못 더함
            
            answer += 1
            return
        
        if index == len(numbers) :
            return
            
        #num1 = num + numbers[index]
        plusorminus(num + numbers[index], index + 1, numbers, target)
        
        #num2 = num - numbers[index] 
        plusorminus(num - numbers[index], index + 1, numbers, target)

def solution(numbers, target):
    
    global answer#전역변수 사용
    answer = 0
    num = 0
    
    plusorminus(num, 0, numbers, target)#인덱스 0 부터 시작
    #plusorminus(num, 0, numbers, target)#이렇게 2번 소환하면 answer가 당연히 2배...
    
    
    return answer #왜 answer가 2배로 나올까? -> 위 문장 참고

print(solution([1, 1, 1, 1, 1], 3))


#또다른 풀이

answer = 0

def DFS(idx, numbers, target, value):
    
    global answer
    N = len(numbers)
    
    if(idx == N and target == value):
        answer += 1
        return
    
    if(idx == N):
        return

    DFS(idx + 1, numbers, target, value + numbers[idx])
    DFS(idx + 1, numbers, target, value - numbers[idx])
    
def solution(numbers, target):
    
    global answer
    DFS(0, numbers, target, 0)
    return answer

print(solution([1, 1, 1, 1, 1], 3))

#또다른 풀이
def solution(numbers, target):
    
    answer = 0
    tree = [0]
    
    for i in numbers :
        child = []
        for j in tree :
            child.append(j + i)
            child.append(j - i)
            
        tree = child
        
    for i in tree :
        if i == target :
            answer += 1
    
    return answer

print(solution([1, 1, 1, 1, 1], 3))