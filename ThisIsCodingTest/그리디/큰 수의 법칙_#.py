N, M, K = map(int, input().split())
l = list(map(int, input().split()))

ans = [0] * M #정답 숫자들 나열한배열
l_count = [0] * 1001 #각 요소들 카운트하는 배열

l.sort(reverse = True)
trial = 0 #차례변수
count = 0 #K 보다 커지는지 확인변수
l_index = 0 #l배열에서의 인덱스

while trial < M :

    if l_count[l[l_index]] < K : 

        ans[trial] = l[l_index]
        trial += 1
        l_count[l[l_index]] += 1

    elif l_count[l[l_index]] == K :

        l_index += 1
        ans[trial] = l[l_index]
        trial += 1
        l_count[l[l_index]] += 1
        l_index -= 1
        l_count[l[l_index]] = 0

sum_num = 0

for i in range(M) :
    sum_num += ans[i]

print(sum_num)
#만약 가장 큰 수와 두번째로 가장 큰 수가 같을 때, 두번째 수를 한번 더하고 나서, 다시 while문 돌릴때 어떻게 두번째 수를 다시 더할지 몰라서 미해결
#index를 초기화해서 당연히 접근 불가
#이럴땐 변수 활용하여 가장 큰 수와 두번째로 가장 큰 수 저장.
#가장 큰 수를 K번 더하고, 두 번째로 큰 수는 한 번만 더하면 됨. 어차피 가장 큰 거만 고려해야해서 두 번째 더하는 순간, K번 넘게 연달아 안 더해짐. -> 그리디

#책 풀이
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse = True)
first = data[0]
second = data[1]

result = 0

while True :
    for i in range(k) :
        if m == 0 :
            break
            
        result += first
        m -= 1
    if m == 0 :
        break
    result += second
    m -= 1

print(result)

#좀 더 효율적으로
#반복되는 수열에 대해서 파악
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse = True)
first = data[0]
second = data[1]

result = 0

#가장 큰 수가 더해지는 횟수 계산
count = m // (k + 1) * k 
count += m % (k + 1)

result += (count) * first #가장 큰 수 더하기
result += (m - count) * second #두번째로 큰 수 더하기
print(result)
