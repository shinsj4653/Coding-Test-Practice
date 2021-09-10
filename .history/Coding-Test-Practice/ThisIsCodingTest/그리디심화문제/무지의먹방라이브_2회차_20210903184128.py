# 시간초과..어떻게 해결??
# -> 시간이 적게 걸리는 음식부터 확인하는 탐욕적 접근방식 필요
# 총 k시간 이랑 지금까지 걸린시간 이랑 비교하는 방식필요

# 무조건 일일히 다 순회한다는 방식보단 -> 짧은 시간부터 고려하는 연습!

import heapq

food_times = [3, 1, 2]
k = 5

# 전체음식을 먹는 시간보다 k가 크거나 같다면 -1
if sum(food_times) <= k:
    print("안녕")
# 위 경우는 네트워크 장애전에 이미 다 먹음..

# 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
q = []
for i in range(len(food_times)):

    # (음식시간, 음식번호) 형태로 -> 튜플
    heapq.heappush(q, (food_times[i], i + 1))

sum_value = 0  # 먹기 위해 사용한 시간
previous = 0  # 직전에 다 먹은 음식 시간

length = len(food_times)  # 남은 음식의 개수

# sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k비교

while k - sum_value <= (q[0][0] * length):
    now = heapq.heappop(q)[0]
    sum_value += now * length
    length -= 1  # 다 먹은 음식 제외
    # previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬
print(result[(k - sum_value) % length][1])
