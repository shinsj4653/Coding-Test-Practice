c = input()
r = (ord(c)-97)
i = 0

for i in range(r - i + 1) :
    print(chr(i + 97), end=" ") #출력하고 엔터X -> 띄어쓰기만 함.

#while문으로 접근
c=input()

n=ord(c)
i=ord('a')

while i<=n :
    print(chr(i), end=' ')
    i+=1