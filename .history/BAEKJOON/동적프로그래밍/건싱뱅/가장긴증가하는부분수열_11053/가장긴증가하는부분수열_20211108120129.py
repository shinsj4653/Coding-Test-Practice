n = int(input())
count = 1

A = list(map(int, input().split()))
max_num = A[0]

for i in range(1, len(A)):

    if A[i - 1] < A[i]:
        A[i] = A[i - 1]

print(count + 1)
