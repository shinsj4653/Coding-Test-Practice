global n 
n = int(input())
global l
l = list(map(int, input().split()))

def findmin(my_list) :

    
    min_num = 100000000000000

    for num in my_list :
        if min_num > num :
            min_num = num

    return min_num


print(findmin(l))