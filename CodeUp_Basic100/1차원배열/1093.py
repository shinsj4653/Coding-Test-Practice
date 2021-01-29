N = int(input())
students = [0] * 23
l = list(map(int, input().split()))
for i in range(N) :
    students[l[i] - 1] += 1
for i in range(0, 23) : 
    print(students[i], end=" ")