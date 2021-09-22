n = int(input())
test = []
d = [0] * 11

for i in range(n):
    test.append(int(input()))
d[1] = 1
d[2] = 2
d[3] = 4

for num in test:
    count = 0 #한자리, 두자리, 세자리 경우의 더하기
    for i in range(1, 4) :
        
