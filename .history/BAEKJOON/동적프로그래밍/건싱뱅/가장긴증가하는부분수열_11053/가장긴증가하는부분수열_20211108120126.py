n = int(input())
count = 1
max_num = A[0]
A = list(map(int, input().split()))

for i in range(1, len(A)):

    if A[i - 1] < A[i]:
        A[i] = A[i - 1]

print(count + 1)
