n = int(input())
count = 1

A = list(map(int, input().split()))
max_num = A[0]

for i in range(1, len(A)):

    if A[i - 1] < A[i]:
        max_num = A[i]
        count += 1
        
    else :
        A[i] = max_num

print(count + 1)
