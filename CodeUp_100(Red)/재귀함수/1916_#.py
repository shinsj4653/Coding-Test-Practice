#함수가 한 번 호출되면 다시 두 번 호출되기 때문에 지수적으로 증가해 O(2^n)이 된다.
def p(N) :

    if N == 1 :
        return 1
    elif N == 2 :
        return 1
    else :
        return p(N - 1) + p(N - 2)

N = int(input())
print(p(N) % 10009)