array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)) :
    
    min_index = i

    for j in range(i + 1, len(array)) :
        
        if array[min_index] > array[j] : #리스트에서 가장 작은 데이터를 찾는 일이 코테에서 자주나옴.
            min_index = j
    
    array[i], array[min_index] = array[min_index], array[i]

print(array)