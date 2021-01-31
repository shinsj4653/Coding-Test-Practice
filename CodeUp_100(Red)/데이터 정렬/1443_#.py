#삽입 정렬
#시간 복잡도 : O(N^2)

#차례가 거듭될수록 탐색 범위가 늘어남.

#2개의 반복문필요
a = []
n = int(input())

for i in range(n) :
    a.append(int(input()))

for end in range(1, len(a)) :
    for i in range(end, 0, -1) :

        if a[i - 1] > a[i] :
            a[i - 1], a[i] = a[i], a[i - 1]

#최적화 : 기존에 있던 값들은 이전 단계에서 모두 정렬되었다는 점 활용
#새롭게 추가된 값보다 작은 숫자를 만나는 최초의 순간까지만 내부 반복문 수행하면됨.
#이렇게 하면 정렬된 배열이 들어올 경우 O(N)의 시간복잡도 달성가능.

a = []
n = int(input())

for i in range(n) :
    a.append(int(input()))

for end in range(1, len(a)) :
    i = end
    while i > 0 and a[i - 1] > a[i] :
        a[i - 1], a[i] = a[i], a[i - 1]
        i -= 1

#추가 최적화 : swap 작업없이 단순히 shift 시키는 것 만으로도 구현가능.
#앞의 값이 정렬된 범위에 추가시킨 값보다 클 경우 앞의 값을 뒤로밀다가 최초의 작은 값을 만나는 순간 그 뒤에 추가된 값을꼽으면됨.
a = []
n = int(input())

for i in range(n) :
    a.append(int(input()))

for end in range(1, len(a)) :
    to_insert = a[end]
    i = end
    while i > 0 and a[i - 1] > to_insert :
        a[i] = a[i - 1]
        i -= 1
    a[i] = to_insert

for i in range(n) :
    print(a[i])