n = int(input())
cantorSet = ["-"] * (3 ** n)
start = 0
end = 3 ** n - 1


def changeSet(n, start, end, cantorSet):

    if " " not in cantorSet[start : end + 1]:
        # 공백이 없으면 공백으로 바꿔줘야
        cantorSet[start + n // 3 : start + n // 3 * 2] = [" "] * (n // 3)
    
    n //= 3

    if n == 1:
        return
    changeSet(n, 0, n - 1, cantorSet)
    changeSet(n, n, n * 2 - 1, cantorSet)
    changeSet(n, n * 2, n * 3 - 1, cantorSet)

if n >= 1 :
    changeSet(3 ** n, start, end, cantorSet)
    for c in cantorSet :
        print('c', end="")
    
elif n == 0:
    print('-')
