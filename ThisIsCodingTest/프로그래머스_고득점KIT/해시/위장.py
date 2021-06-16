def solution(clothes):
    answer = 1
    c_dict = dict()
    
    for name, kind in clothes :
        if kind not in c_dict :
            c_dict[kind] = 1
            
        else :
            c_dict[kind] += 1
    
    
    for kind in c_dict :
        
        answer *= c_dict[kind] + 1
        #안 입는 경우까지 포함
    
    
    
    return answer - 1

#모든 경우 더하기 -> 1개씩 입는 경우
#모든 경우 곱하기 -> 모두 입는경우
#이렇게 되면 2종류, 3종류는 미포함하게 됨!