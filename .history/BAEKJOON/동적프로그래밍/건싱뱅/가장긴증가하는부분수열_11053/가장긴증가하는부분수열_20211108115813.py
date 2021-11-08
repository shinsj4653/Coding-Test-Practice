n = int(input())
count = 0

A = list(map(int, input().split()))

for i in range(len(A) - 1):
    if A[i] < A[i + 1]:
        count += 1

print(count)
