#변수명 많을때는 변수 사용 헷갈리지 않도록 주의
n = int(input())
coin_list = list(map(int, input().split()))

max_coin = max(coin_list)
sum_list = [False] * (max_coin + 1)
coin_list.sort()

for i in range(len(coin_list) - 1) :
    price = coin_list[i]
    for j in range(i + 1, len(coin_list)) :
        
        price += coin_list[j]
        
        if price > max_coin :
            continue

        sum_list[price] = True

    sum_list[coin_list[i]] = True

sum_list[coin_list[len(coin_list) - 1]] = True

for i in range(1, len(sum_list)) :
    if sum_list[i] == False :
        print(i)
        break