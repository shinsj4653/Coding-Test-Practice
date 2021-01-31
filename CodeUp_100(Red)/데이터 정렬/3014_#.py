#값의 범위가 적을때 사용하는 비둘기집 정렬(값의 범위가 0 ~ 100,000)
N = int(input())

maxinput = 0

l = list(map(int, input().split()))#이 값들을 배열의 인덱스로 활용

ans = [0] * 100000#값의 개수

for i in range(N) : 
    ans[l[i]] += 1
    if(l[i] > maxinput) :
        maxinput = l[i]
    
for i in range(maxinput + 1) :
    for j in range(ans[i]) : 
        print(i, end = " ")
    print()