n = int(input())
h = 0 #백의 자릿수

t = n // 10 #십의 자릿수
o = n % 10 #일의 자릿수

n = (o * 10 + t) * 2

if n >= 100 :
    h = n // 100
    n = n - h * 100

if n <= 50 :
    print(n)
    print("GOOD")
else :
    print(n)
    print("OH MY GOD")

