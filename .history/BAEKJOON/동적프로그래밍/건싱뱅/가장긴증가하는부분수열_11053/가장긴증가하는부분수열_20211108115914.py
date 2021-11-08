n = int(input())
count = 0

A = list(map(int, input().split()))

for i in range(1, len(A)):
    if A[i - 1] < A[i]:
        count += 1

print(count + 1)
