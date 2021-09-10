def solution(gems):
    answer = []
    
    g = set(gems)#변수이름 제발 중복되지 않게. 안그러면 헷갈림..
    
    g_dict = dict()
    
    for gem in g :
        g_dict[gem] = 1
    
    idx = 0
    start = 0
    end = 0
    print(len(g))
    
    for gem in gems :
        
        if g_dict[gem] == 1 :
            g_dict[gem] -= 1
        
        
        if sum(g_dict.values()) == 0 :
            end = idx + 1
            break
        
        else :
            idx += 1
            
   
    
    for idx in range(end - 1, -1, -1) :
        if g_dict[gems[idx]] == 0 :
            g_dict[gems[idx]] += 1
                
        if sum(g_dict.values()) == len(g) :
            start = idx + 1
            break
            
            
        
    answer.append(start)
    answer.append(end)
    
    return answer

#print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
#끝자리를 구하고, 반대로 하여 앞자리 구하기..-> 효율성대실패

#인터넷 풀이
#더블 포인터사용
#이렇게 하면 2번 탐색할 필요x
def solution(gems):
    answer = []
    
    g = set(gems)#변수이름 제발 중복되지 않게. 안그러면 헷갈림..
    dic = {gems[0] : 1}
    size = len(g)
    answer = [0, len(gems) - 1]
    
    start, end = 0, 0
    
    while start < len(gems) and end < len(gems) :
        if len(dic) == size :
            if end - start < answer[1] - answer[0] :
                answer = [start, end]
            
            if dic[gems[start]] == 1 :
                del dic[gems[start]]
            
            else :
                dic[gems[start]] -= 1
            
            start += 1
        
        else :
            end += 1
            if end == len(gems) :
                break
            
            if gems[end] in dic.keys() :
                dic[gems[end]] += 1
            
            else :
                dic[gems[end]] = 1
    
    return [answer[0] + 1, answer[1] + 1]