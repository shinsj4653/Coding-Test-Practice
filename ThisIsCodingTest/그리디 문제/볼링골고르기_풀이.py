#조합의 원리 이해필요
#무게마다 볼링공 몇개 있는지 파악 -> 리스트활용
#단계마다 B가 선택하는 경우의 수 줄어듦 -> 조합의 원리 땜에

n, m = map(int, input().split())
data = list(map(int, input().split()))

#1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data :

    array[x] += 1

#1부터 m까지의 각 무게에 대하여 처리

for i in range(1, m + 1) :
    n -= array[i] #A가 선택하는 경우 제외 -> 조합이라서 서로 다른 무게를 골라야해서
    result += array[i] * n #A가 선택하는 경우 * B가 선택하는 경우

print(result)

