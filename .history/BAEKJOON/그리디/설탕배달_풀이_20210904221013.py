sugar = int(input())

bag = 0
while sugar >= 0:
    if sugar % 5 == 0:
        bag += sugar // 5
        print(bag)
        break  # 밖의 else문으로 안감!
    sugar -= 3
    bag += 1  # 5의 배수가 될 때 까지 설탕 -3, 봉지 += 1

else:  # 이런식으로 짜면, 4같은 예외를 처리가능!
    print(-1)
