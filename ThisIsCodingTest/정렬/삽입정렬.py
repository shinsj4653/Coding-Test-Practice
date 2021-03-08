#선택정렬에 비해 실행시간이 더 짧음.
#특히 필요할 때만 위치를 바꾸므로 데이터가 거의 정렬되어 있을 때 훨씬 효율적
#거의 정렬되어 있을땐 퀵정렬보다도 더 강력

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)) :
    
    for j in range(i, 0, -1) :

        if array[j] < array[j - 1] :
            array[j], array[j - 1] = array[j - 1], array[j]

        else :  #자기보다 작은 데이터 만나면 그 자리에서 멈춤.
            break

print(array)
