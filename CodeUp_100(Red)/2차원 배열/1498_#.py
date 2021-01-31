#테스트케이스 중 하나에서 오류남.

n, g = map(int, input().split())
arr = list(map(int, input().split()))
new_arr = [0] * (int(format(n / g, ".0f")))

i = 0
new_arr_i = 0
min_num = 1000

while i < len(arr) :
    

    if min_num > arr[i] :
        min_num = arr[i]

    i += 1

    if i % g == 0 :
        new_arr[new_arr_i] = min_num
        min_num = 1000
        new_arr_i += 1
    
    elif i == len(arr) :
        new_arr[new_arr_i] = min_num


for k in range(len(new_arr)) :

    print(new_arr[k], end = " ")

    
    
    


