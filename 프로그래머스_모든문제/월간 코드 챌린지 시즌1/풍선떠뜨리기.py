# global count 
# count = 0

# #def quick_sort(l, left, right) :
# def quick_sort(l, start, end) : #left, right말고 start랑 end로! 그래야 종료조건도 작성가능
    
    
#     if start >= end :
#         return 
    
#     global count
#     pivot = start
#     left = start + 1
#     right = end
    
    
#     while left <= right :
        
#         if l[left] <= l[pivot] and left <= end: 
#             left += 1
            
#         if l[right] >= l[pivot] and right > start :
#             right -= 1
        
#         if left > right :
#             l[pivot], l[right] = l[right], l[pivot]
#             count += 1
            
        
#         else :
#             l[left], l[right] = l[right], l[left]
#             count += 1
    
#     quick_sort(l, start, right - 1)
#     quick_sort(l, right + 1, end)
    
# l_list = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
# print(quick_sort(l_list, 0, len(l_list) - 1))
# print(count)

def solution(a):
    answer = 0
    #아이디어 : 자신의 어느 한쪽방향이든 자신보다 크면 자신은 살아남기 가능
    INF = int(1e9)
    
    result = [False for _ in range(len(a))]
    
    minFront, minRear = INF, INF
    
    for i in range(len(a)):
        
        if a[i] < minFront:
            minFront = a[i]
            result[i] = True
            
        if a[-1 - i] < minRear:
            minRear = a[-1 - i]
            result[-1 - i] = True
    
    for r in result :
        if r == True :
            answer += 1
    
    return answer