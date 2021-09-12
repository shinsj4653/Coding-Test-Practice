n = int(input())
chicken = list(map(int, input().split()))
k = int(input())

count = n // 2  # 정렬을 하는 사람의 수

while True:

    # 마지막에 if count == k 이면 break
    if count == k:
        break

print(chicken)
