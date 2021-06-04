#조합사용법
from itertools import combinations

n, m = map(int, input().split())
ball_list = list(map(int, input().split()))


result = list(combinations(ball_list, 2))

count = 0 

for i in range(len(result)) :
    if result[i][0] == result[i][1] :
        continue
    count += 1

print(count) 