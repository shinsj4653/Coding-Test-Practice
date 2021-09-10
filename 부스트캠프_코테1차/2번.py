def solution(l) :
    
    answer = ''
    total = 0
    type_list = []
    current = ""
    count = 0
    
    for typ in l :
        count += 1
        
        if typ == 'BOOL' :
            total += 1
            
            if total > 128 :
                answer = 'HALT'
                return answer
            
            current += '#'
            
            
                
            
        
        elif typ == 'SHORT' :
            total += 2
            if total > 128 :
                answer = 'HALT'
                return answer
            
            if len(current) == 0 or len(current) == 2 or len(current) == 4 or len(current) == 6:
                current += '##'
                
            elif len(current) == 1 or len(current) == 3 or len(current) == 5 or len(current) == 7:
                current += '.##'

                            
            
                
            
            
        elif typ == 'FLOAT' :
            total += 4
            if total > 128 :
                answer = 'HALT'
                return answer
            
            if len(current) == 0 or len(current) == 4:
                current += '####'
                
            elif 1 <= len(current) <= 3  :
                
                c = ''
                for i in range(4 - len(current)) :
                    c += '.'
                    
                current += c
                current += '####'
                
            elif 5 <= len(current) <= 7  :
                
                c = ''
                for i in range(8 - len(current)) :
                    c += '.'
                    
                current += c
                current += '####'
                
                                
        
        elif typ == 'INT' :
            total += 8
            if total > 128 :
                answer = 'HALT'
                return answer
            
            if len(current) == 0 :
                current += '########'
            
        elif typ == 'LONG' :
            total += 16
            if total > 128 :
                answer = 'HALT'
                return answer
            
            if len(current) == 0 :
                current += '########'
                
            
        
            
        if len(current) == 8 :
            
            if typ == 'LONG' :
                type_list.append(current)
                type_list.append(current)
                current = ''
                
            else :
                type_list.append(current)
                current = ''
                
        
        
        #마지막이면    
        if count == len(l):
            c = ''
            if len(current) >= 1 :
                for i in range(8 - len(current)) :
                    c += '.'
            
            current += c
            type_list.append(current)
                
        
            
                
        
    answer = (",").join(type_list)
    
    
    
    return answer


print(solution(['INT', 'INT', 'BOOL', 'SHORT', 'FLOAT', 'LONG']))
print()
print(solution(['BOOL', 'FLOAT', 'SHORT', 'SHORT', 'FLOAT', 'BOOL']))
