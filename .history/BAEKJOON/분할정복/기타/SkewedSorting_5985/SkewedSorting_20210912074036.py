# sort를 할 시에 dist에 플러스 -> 각 단계 리스트 개수의 반 값을 한거를 곱합
# 첫 번째 값이 두 번째 값보다 클때만 swap

n = int(input())
cowList = []
dist = 0

for i in range(n):
    cowList.append(int(input()))

for i in range(2^n) :
    
    

print(dist)
