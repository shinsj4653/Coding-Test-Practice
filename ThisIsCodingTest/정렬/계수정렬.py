#특정 조건이 부합할때만 사용가능하지만, 매우빠름.
#데이터의 크기가 한정적이고, 데이터의 크기가 많이 중복되어 있을수록 유리함.
#모든 원소의 값이 0보다 크거나 같다고 가정.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count = [0] * (max(array) + 1)

for i in range(len(array)) :
    count[array[i]] += 1

for i in range(len(count)) :
    for j in range(count[i]) :
        print(i, end = ' ')