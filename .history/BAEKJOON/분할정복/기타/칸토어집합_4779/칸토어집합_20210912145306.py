# 파이썬 문자열 -> 상수여서 바꾸려면 replace()사용해야!
# 리스트 쓰면 메모리 초과...문자열 사용하여 풀기!
# 결국 결과는 '- -' 꼴 -> 굳이 문자열의 3분의 1지점에서 공백변환 필요x

# 문자열 썼는데도 메모리 초과..


# from sys import stdin, setrecursionlimit

# setrecursionlimit(10 ** 6)


# def changeSet(n, start, cantorSet):

#     if cantorSet == " " or cantorSet == "-" or "-" not in cantorSet:
#         return cantorSet

#     else:
#         # 공백이 없으면 공백으로 바꿔줘야
#         arr1 = "-" * (n // 3)
#         arr2 = " " * (n // 3)
#         arr3 = "-" * (n // 3)

#         if n // 3 == 1:
#             return arr1 + arr2 + arr3

#         n //= 3

#         return (
#             changeSet(n, start, arr1)
#             + changeSet(n, start + n, arr2)
#             + changeSet(n, start + n * 2, arr3)
#         )


# while True:
#     n = stdin.readline().rstrip()
#     if n == "":
#         break

#     n = 3 ** int(n)

#     cantorSet = "-" * n
#     start = 0
#     end = n - 1
#     newSet = changeSet(n, start, cantorSet)

#     for c in newSet:
#         print(c, end="")

# 밑 : 인터넷풀이

# 3등분 먼저 하고, 그에 따른 처리 각각!
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def div(s, idx):
    ls = len(s)
    if ls == 3 and idx != 1:
        return "- -"
    elif ls >= 3 and idx == 1:
        return s.replace("-", " ")

    arr = []

    for i in range(0, ls, ls // 3):  # for문 증감식에 ls // 3 -> 3배수씩
        arr.append(string[i : i + ls // 3])

    k = div(arr[0], 0) + div(arr[1], 1) + div(arr[2], 2)
    return k


while 1:
    k = "-"
    n = stdin.readline().rstrip()
    if n == "":
        break
    num = 3 ** int(n)
    if num == 1:
        print("-")
        continue

    string = k * num
    arr = div(string, 0)
    print(arr)
