n = int(input())
n_list = list(map(int, input().split()))
#이진탐색 사용하려면, n_list을 정렬해야함. -> 개념을 문제에 적용하는 연습!!!!!!
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))


def binary_search(array, target, start, end) :

    if start > end : 
        return None
    
    mid = (start + end) // 2

    if array[mid] == target :
        return mid

    elif array[mid] > target :
        return binary_search(array, target, start, mid - 1)

    else :
        return binary_search(array, target, mid + 1, end)



for i in range(m) :

    num = binary_search(n_list, m_list[i], 0, len(n_list) - 1)
    
    if num == None :
        print("no", end = ' ')

    else :
        print("yes", end = ' ')

#방법 2 : 계수 정렬 활용


n = int(input())
n_list = list(map(int, input().split()))


m = int(input())
m_list = list(map(int, input().split()))

array = [0] * 1000000

for i in range(n) :
    array[n_list[i]] = 1

for num in m_list :

    if array[num] == 1 :
        print('yes', end = ' ')
    
    else :
        print('no', end = ' ')


#방법 3 : set 함수이용 -> 단순히 특정한 데이터가 존재하는 검사할때 매우 유용.

n = int(input())
n_set = set(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

for i in m_list :
    if i in n_set :
        print('yes', end = ' ')
    
    else :
        print('no', end = ' ')
