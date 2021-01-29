price = int(input())
i_price = price
days = int(input())
l = list(map(int, input().split()))

for i in range(days) : 
    price = price * (1 + l[i] * (1 / 100))

ans = int(format(price - i_price, ".0f"))

print(ans)
if(ans > 0) :
    print("good")
elif(ans == 0) : 
    print("same")
else : 
    print("bad")

#수학에서의 곱하기 생략 하지 않도록 주의
