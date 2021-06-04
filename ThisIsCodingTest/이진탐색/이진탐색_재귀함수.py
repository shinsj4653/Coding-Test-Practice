#탐색범위가 큰 상황에서의 탐색을 가정하는 문제가 많다.
#처리해야 하는 데이터의 개수나 값이 1,000만 단위 이상으로 넘어가면 이진탐색과 같이 O(logN)의 속도를 내야하는 알고리즘 필요.
def binary_search(array, target, start, end) :
    if start > end : 
        return None
    
    mid = (start + end) // 2

    if array[mid] == target :
        return mid
    
    elif array[mid] > target : #mid기준으로 왼쪽부분만 탐색
        return binary_search(array, target, start, mid - 1)

    else :
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result = None :
    print("원소존재x")

else :
    print(result + 1)

    
