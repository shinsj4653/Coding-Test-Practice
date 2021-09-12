sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += sugar // 5
        print(bag)  # 이 구문으로 오는 순간, 이미 -1 은 아닌게 확정!
        break  # 밖의 else문으로 안감!
    sugar -= 3
    bag += 1  # 5의 배수가 될 때 까지 설탕 -3, 봉지 += 1

else:  # 이런식으로 짜면, 1,2,4같은 예외를 처리가능!
    print(-1)
