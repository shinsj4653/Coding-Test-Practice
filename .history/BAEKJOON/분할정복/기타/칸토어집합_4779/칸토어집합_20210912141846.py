# 파이썬 문자열 -> 상수여서 바꾸려면 replace()사용해야!
# 리스트 쓰면 메모리 초과...문자열 사용하여 풀기!
# 결국 결과는 '- -' 꼴 -> 굳이 3분의 1지점에서 공백변환 필요x

from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def changeSet(n, start, end, cantorSet):

    if cantorSet == " " or cantorSet == "-" or "-" not in cantorSet:
        return cantorSet

    else:
        # 공백이 없으면 공백으로 바꿔줘야
        arr1 = "-" * (n // 3)
        arr2 = " " * (n // 3)
        arr3 = "-" * (n // 3)

        if n // 3 == 1:
            return arr1 + arr2 + arr3

        n //= 3

        return (
            changeSet(n, start, start + n - 1, arr1)
            + changeSet(n, start + n, start + n * 2 - 1, arr2)
            + changeSet(n, start + n * 2, start + n * 3 - 1, arr3)
        )


while True:
    n = stdin.readline().rstrip()
    if n == "":
        break

    n = 3 ** int(n)

    cantorSet = "-" * n
    start = 0
    end = n - 1
    newSet = changeSet(n, start, end, cantorSet)

    for c in newSet:
        print(c, end="")
