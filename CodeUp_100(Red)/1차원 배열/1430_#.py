# N = int(input())
# l = [0] * 10000000

# N_list = list(map(int, input().split()))

# for i in range(len(N_list)) : 
#     l[N_list[i]] = 1

# M = int(input())

# M_list = list(map(int, input().split()))

# for i in range(len(M_list)) :
#     print(l[M_list[i]], end = " ")

#위의 메모리 초과 문제 해결
#입력의 개수가 많은 경우에는 단순히 input()함수를 그대로 사용x
#sys.stdin.readline() 함수이용

import sys

N = int(input())
N_list = list(map(int, (sys.stdin.readline().rstrip()).split()))
M = int(input())
M_list = list(map(int, (sys.stdin.readline().rstrip()).split()))

for i in M_list :
    
    if i in N_list :
        print(1, end = ' ')
    else : 
        print(0, end = ' ')
    
