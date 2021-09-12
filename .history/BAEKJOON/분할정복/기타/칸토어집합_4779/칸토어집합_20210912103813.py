n = int(input())
cantorSet = ["-"] * (3 ** n)
start = 0
end = 3 ** n - 1


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


changeSet(3 ** n, start, end, cantorSet)
for c in cantorSet:
    print(c, end="")
