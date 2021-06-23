# def solution(N, number):
#     answer = 0
    
#     d = [[0] * number for i in range(N + 1)]
    
#     #i:number, j:N
#     d[0][0] = 1
#     d[1][1] = 1
#     d[1][2] = 2
#     d[1][3] = 2
#     d[1][4] = 2
#     d[1][5] = 2
#     d[1][6] = 2
#     d[1][7] = 2
#     d[1][8] = 2
#     d[1][9] = 2
    
#     for i in range(2, number + 1) :
#         for j in range(1, N + 1) :
            
#             if j == 1 :
#                 d[i][j] = j
                
#             elif i == j :
#                 d[i][j] = 1
                
#             else : 
#                 if (i * 10 + i) % i != 0 :
                    
                
#     answer = d[number][N] 
          
    
#     return answer

#포기..밑에 풀이

def solution(N, number):
    answer = 0
    
    if N == number :
        return 1
    
    s = [set() for x in range(8)]
    
    for i, x in enumerate(s, start = 1) :
        x.add(int(str(N) * i))
    
    for i in range(1, 8) :
        for j in range(i) :
            for op1 in s[j] :
                for op2 in s[i - j - 1] :
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0 :
                        s[i].add(op1 // op2)
                        
        if number in s[i] :
            answer = i + 1
            break
            
    else :
        answer = -1
                    
        
    
    return answer

print(solution(5, 12))