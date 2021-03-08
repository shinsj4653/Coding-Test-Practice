n = int(input())
#n의 범위가 100,000이면, 최악의 경우 O(NlogN)을 보장하는 알고리즘, 혹은 O(N)을 보장하는 계수정렬 활용하면됨.

students = dict()

for i in range(n) :
    array = list(input().split())
    students[array[0]] = int(array[1])

students = sorted(students, key = lambda x : x[1])
print(students)


#책풀이
#튜플자료형을 리스트에 넣어 풀어도 됨.
n = int(input())

array = []
for i in range(n) :
    input_data = input().split() #split()함수가 리스트 반환
    array.append((input_data[0], int(input_data[1]))

array = sorted(array, key = lambda student : student[1]) #key를 활용하여 점수를 기준으로 정렬

for students in array :
    print(student[0], end = ' ')

#튜플활용하여 students[1], students[0]으로 바로바로 접근가능.
