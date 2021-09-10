#find() 함수 -> 없으면 -1반환
#리스트에서는 in 아니면 not in 으로 확인

answer = 0 
def word_dfs(begin, target, words, visited) :
    
    global answer
    stacks = [begin]
    
    while stacks :
        
        stack = stacks.pop()
        
        if stack == target :
            return answer
        
        for w in range(0, len(words)) :
            
            if len([i for i in range(0, len(words[w])) if words[w][i] != stack[i]]) == 1 :
                #이 방식으로 알파벳 하나만 다를 때를 판별!
                
                if visited[w] != 0 :
                    continue
                    
                visited[w] = 1
                
                stacks.append(words[w])
        
    
    
        answer += 1



def solution(begin, target, words):
    
    #각 루트에서 어느 경로의 탐색에서 제일 빨리 target 단어까지 변환되는지 찾아야한다 -> dfs활용
    global answer
    
    if target not in words : 
        return 0 
        
    visited = [0 for i in words]
    
    word_dfs(begin, target, words, visited)
    
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))