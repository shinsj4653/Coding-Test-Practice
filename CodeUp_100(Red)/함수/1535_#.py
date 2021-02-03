#.index() 사용법 : 리스트이름.index(리스트요소)
global n 
n = int(input())
global l
l = list(map(int, input().split()))

def findmax(my_list) :

    index = 0
    max_num = -1000000000

    for num in my_list :
        if max_num < num :
            max_num = num
            index = my_list.index(num)

    return index


print(findmax(l) + 1)