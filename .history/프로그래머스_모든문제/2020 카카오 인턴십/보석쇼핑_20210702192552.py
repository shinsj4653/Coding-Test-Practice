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
    #print(sum(g_dict.values()))
    for gem in gems :
        
        if g_dict[gem] == 1 :
            g_dict[gem] -= 1
        
        #print(sum(g_dict.values()))
        if sum(g_dict.values()) == 0 :
            end = idx + 1
            break
        
        else :
            idx += 1
            
    #print(g_dict)
    
    for idx in range(end - 1, -1, -1) :
        if g_dict[gems[idx]] == 0 :
            g_dict[gems[idx]] += 1
        
        #print("sum : " , sum(g_dict.values()))
        #print(idx)
                
        if sum(g_dict.values()) == len(g) :
            start = idx + 1
            break
            
            
        
    answer.append(start)
    answer.append(end)
    
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))