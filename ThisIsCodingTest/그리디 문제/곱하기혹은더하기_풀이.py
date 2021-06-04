#두 수에 대한 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며,
#두 수 모두 2이상인 경우에는 곱하기!

data = input()

result = int(data[0]) #두 수를 비교해야 할때는, 처음에 result 변수에 첫 수를 먼저 대입하고 시작
#int(data[0]) 이 방식활용!

for i in range(1, len(data)) : #문자 index 1 자리부터 끝까지
    
    num = int(data[i]) #for문 안에서 변수사용하여 하나씩 뽑아오는 방식활용
    
    if num <= 1 or result <= 1 :
        result += num
    
    else :
        result *= num

print(result)
