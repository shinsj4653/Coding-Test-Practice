# import heapq

# a, b, c = map(int, input().split())
# multiplyList = []
# heapq.heappush(multiplyList, (a, b))  # (0, 1) -> 곱할 수, 곱할 횟수
# resultList = []

# while True:

#     num, multiplyCount = heapq.heappop(multiplyList)

#     if multiplyCount == 2:
#         resultList.append(num * num)
#         break

#     else:
#         if multiplyCount % 2 != 0:
#             resultList.append(num)
#             num *= num
#             multiplyCount //= 2
#             multiplyList.append((num, multiplyCount))

#         else:
#             num *= num
#             multiplyCount //= 2
#             multiplyList.append((num, multiplyCount))

# # (a * b) mod n  = ((a mod n) * (a mod n)) mod n

# result = 1
# for num in resultList:
#     result = result * (num % c)

# print(result % c)

# 밑 인터넷 풀이
def power(a, b):
    if b == 1:  # b의 값이 1이면 a % C를 return한다.
        return a % C
    else:
        temp = power(a, b // 2)  # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % C  # b가 짝수인 경우
        else:
            return temp * temp * a % C  # b가 홀수인 경우


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = power(A, B)
    print(result)
