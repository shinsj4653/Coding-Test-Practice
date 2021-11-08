n = int(input())
length = 0

A = list(map(int, input().split()))
max_num = A[0]

for i in range(len(A)):

    if max_num < A[i]:
        max_num = A[i]
        length += 1

    else:
        A[i] = max_num

print(length)
