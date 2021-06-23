def solution(triangle):
    answer = 0
    
    s_tree = [[0] * len(row) for row in triangle]
    s_tree[0][0] = triangle[0][0]
    row_sum = 0
    
    for row in range(1, len(triangle)) :
        
            
            
        s_tree[row][0] = s_tree[row - 1][0] + triangle[row][0]
        s_tree[row][row] = s_tree[row - 1][row - 1] + triangle[row][row]
        
        
        if row >= 2 :    
            for i in range(1, row) :
                s_tree[row][i] = max(s_tree[row - 1][i - 1], s_tree[row - 1][i]) + triangle[row][i]
            
        if row == len(triangle) - 1:
            answer = max(s_tree[row])
            

    
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

#오랜만에 통과!!!
#더 좋은 밑 풀이

dp = []
for t in range(1, len(triangle)) :
    for i in range(t + 1) :
        if i == 0 :
            triangle[t][0] += triangle[t - 1][0]
            
        elif i == t :
            triangle[t][-1] += triangle[t - 1][-1]
            
        else :
            triangle[t][i] += max(triangle[t - 1][i - 1], triangle[t - 1][i])
            
    
return max(triangle[-1])
