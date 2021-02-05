#에라토스테네스의 체 접근 방법 사용했지만, 실패..


a, b = map(int, input().split())
l = [True for i in range(b + 1)]

for i in range(1, b + 1) :

    num = i // 1000 + i // 100 + i // 10 + i // 1 + i # 이러면 1111 일때 i // 100 은 11 이 됨. 자릿수를 반환하지 않음.
    if num <= b and l[num] == True:
        l[num] = False

sum_num = 0

for i in range(a, b + 1) :
    
    if l[i] == True : 
        sum_num += i

print(sum_num)

#풀이
#각 자릿수 더해주는 알고리즘이 틀림

a, b = map(int, input().split())
l = [True for i in range(b + 1)]

for i in range(1, b + 1) :

    temp_a = i
    temp_b = 0
    num = 0

    while temp_a > 0 :
        temp_b += temp_a % 10 # 10으로 나눈 나머지가 1의 자릿수
        temp_a = temp_a // 10 # 10으로 나눈 몫으로 수를 변경 -> 또 10으로 나누면 나머지는 원래 수의 10의 자릿수 반환.

    num = i + temp_b

    if num <= b and l[num] == True :
        l[num] = False

sum_num = 0

for i in range(a, b + 1) :
    
    if l[i] == True : 
        sum_num += i

print(sum_num)
