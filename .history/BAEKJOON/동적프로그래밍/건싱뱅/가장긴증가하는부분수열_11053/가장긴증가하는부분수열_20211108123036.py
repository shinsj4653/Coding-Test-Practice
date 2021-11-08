n = int(input())
length = 0

A = list(map(int, input().split()))
max_num = A[0]

for i in range(1, len(A)):

    if max_num < A[i]:
        max_num = A[i]
        if i == 1:
            length += 2
        else:
            length += 1

    else:
        A[i] = max_num

print(length)
