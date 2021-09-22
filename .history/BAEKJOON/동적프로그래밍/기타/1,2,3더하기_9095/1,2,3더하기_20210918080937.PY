n = int(input())
test = []
d = [0] * 11

for i in range(n):
    test.append(int(input()))
d[1] = 1
d[2] = 2

for num in test:
    for i in range(3, num) :
        
