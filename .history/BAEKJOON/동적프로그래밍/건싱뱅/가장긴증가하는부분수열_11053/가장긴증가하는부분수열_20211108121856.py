n = int(input())
count = 0

A = list(map(int, input().split()))
max_num = A[0]

for i in range(1, len(A)):

    if max_num < A[i]:
        max_num = A[i]
        count += 1

    else:
        A[i] = max_num

print(count)
