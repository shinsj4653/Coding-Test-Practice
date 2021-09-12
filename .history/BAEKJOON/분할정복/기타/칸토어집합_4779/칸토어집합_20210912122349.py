# 파이썬 문자열 -> 상수여서 바꾸려면 replace()사용해야!
# 리스트 쓰면 메모리 초과...문자열 사용하여 풀기!
# 결국 결과는 '- -' 꼴 -> 굳이 3분의 1지점에서 공백변환 필요x

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def changeSet(n, start, end, cantorSet):

    if " " not in cantorSet[start : end + 1]:
        # 공백이 없으면 공백으로 바꿔줘야
        cantorSet[start + n // 3 : start + n // 3 * 2] = " " * (n // 3)

    n //= 3

    if n == 1 or n == 0:
        return

    changeSet(n, start, start + n - 1, cantorSet)
    changeSet(n, start + n, start + n * 2 - 1, cantorSet)
    changeSet(n, start + n * 2, start + n * 3 - 1, cantorSet)


while True:
    n = stdin.readline().rstrip()
    if n == "":
        break

    n = 3 ** int(n)

    cantorSet = "-" * n
    start = 0
    end = n - 1
    changeSet(n, start, end, cantorSet)

    for c in cantorSet:
        print(c, end="")
