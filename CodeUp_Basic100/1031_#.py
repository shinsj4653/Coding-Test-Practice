#10진수를 2진수로 : bin(n)
#8진수로 : oct(n)
#16진수로 : hex(n)

#위 3개는 0b1000,0o40,0x20 이런 형태로 출력됨.

#format함수로 해야 int형으로 나옴.
#print(format(n,'b')) 2진수
#print(format(n,'o')) 8진수
#print(format(n,'x')) 16진수

#n은 int형이여야!

n = input()
print(format(int(n),'o'))