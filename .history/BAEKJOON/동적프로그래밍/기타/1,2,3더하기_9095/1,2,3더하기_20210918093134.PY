n = int(input())
test = []
d = [0] * 11
d[1] = 1
d[2] = 2

for i in range(n):
    test.append(int(input()))

for num in test:
    count = 0 #한자리, 두자리, 세자리 경우의 더해서 dp 테이블에 대입
    for i in range(1, num + 1) :
        
