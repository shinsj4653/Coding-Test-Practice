#연속된 세개의 계단을 밟을 수 없으므로..
#n - 1 번째 계단을 밟으면, n - 2 계단은 밟지 못한다. n - 3 번째 계단을 밟아야한다.
#f(n) = f(n - 3) + stair[n - 1] + stair[n]
#n - 1 번째 계단을 밟지 않으면, n - 2계단을 무조건 밟는다.
#f(n) = f(n - 2) + stair[n]
#f(n - 3)과 f(n - 2)는 지금까지 해당 계단을 오르는 경우의 수들의 값 중, 점수가 가장 커야함.


#각 번 째의 계단에서의 최댓값 필요 -> max() 내장함수 이용

stair = [0] * 301 #계단값 저장.
point_list = [0] * 301 #메모


def recur(num) :
    if num < 0 :
        return 0
    if num == 1 :
        point_list[num] = stair[num]
        return point_list[1]
    if num == 2 :
        point_list[num] = stair[num] + stair[num - 1]
        return point_list[num]

    if point_list[num] != 0 :
        return point_list[num]

    else :
        point_list[num] = max(stair[num - 1] + stair[num] + recur(num - 3) , stair[num] + recur(num - 2))
        return point_list[num]
    


num = int(input())

for i in range(1, num + 1) :
    stair[i] = int(input())

print(recur(num))

