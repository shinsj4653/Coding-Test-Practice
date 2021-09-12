# 파이썬 문자열 -> 상수여서 바꾸려면 함수 사용해야

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def changeSet(n, start, end, cantorSet):

    if " " not in cantorSet[start : end + 1]:
        # 공백이 없으면 공백으로 바꿔줘야
        cantorSet[start + n // 3 : start + n // 3 * 2] = [" "] * (n // 3)

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

    cantorSet = ["-"] * n
    start = 0
    end = n - 1
    cantorSet = changeSet(n, start, end, cantorSet)

    for c in cantorSet:
        print(c, end="")
