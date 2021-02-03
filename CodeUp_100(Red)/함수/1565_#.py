#최소공배수 : CodeUp_Basic 100 > 종합 > 1092 문제
#주어진 수 들을 나눴을 때 모두 나머지가 0이 되는 수

#이 함수는 유클리드 호제법 사용
#x % y == 0 이라면 gcd(x, y) = y성립
#x % y != 0 이라면 gcd(x, y) = gcd(y, x % y)

def gcd(p, q) :

    if p % q == 0 : #이 때에는 q 가 최대공약수
        
        return q
    
    return gcd(q, p % q) #나누어 안 떨어지면 q , p % q 를 다음수로

def lcm(a, b) :
    return a * b // gcd(a, b)# // 써야 int형이 나옴. / 쓰면 실수형으로 됨.


a, b = map(int, input().split())
print(lcm(a, b))