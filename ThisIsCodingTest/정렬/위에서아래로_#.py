n = int(input())
li = []

for i in range(n) :
    li.append(int(input()))

li.sort(reverse=True)
#sorted()함수는 집합이나 딕셔너리를 입력받아도 반환되는 결과는 리스트

for i in range(n) :
    print(li[i], end = ' ')