N, C = map(int, input().split())
students = list(map(int, input().split()))

students.sort()

total = 0
while total <= N - 1 :
    
    print(students[total], end = " ")
    total += 1

    if total % C == 0 :
        print()