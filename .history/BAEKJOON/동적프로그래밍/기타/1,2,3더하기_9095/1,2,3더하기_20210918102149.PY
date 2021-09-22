n = int(input())
test = []
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(n):
    test.append(int(input()))


for num in test:
    sum = 0

    if num == 1 or num == 2 or num == 3:
        print(d[num])
    else:
        for i in range(1, num):
            if d[i] != 0:
                sum += d[i]
            else:
                for j in range(1, i):
                    temp = 0
                    temp += d[j]
                d[i] = temp
                sum += d[i]

        print(sum)
