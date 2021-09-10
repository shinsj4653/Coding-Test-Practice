#그리디에 익숙하지 않으면 떠올리기 힘든 문제..
#이 유형암기!

#화폐 단위가 작은 동전부터 더해가면서 target변수 업데이트!

n = int(input())
coin = list(map(int, input().split()))
target = 1
coin.sort()

for c in coin :
    if c < target :
        break
    
    target += c

print(target)