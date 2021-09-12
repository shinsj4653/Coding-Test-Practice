n = int(input())
cantorSet = ["-"] * (3 ** n)
start = 0
end = 3 ** n - 1


def changeSet(n, start, end, cantorSet):
    if " " not in cantorSet[start : end + 1]:
        # 공백이 없으면 공백으로 바꿔줘야
        cantorSet[n // 3 : n // 3 * 2] = [" "] * (n // 3)

    n //= 3
    changeSet()
