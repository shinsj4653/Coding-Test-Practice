c = input()
r = (ord(c)-97)
i = 0

for i in range(r - i + 1) :
    print(chr(i + 97), end=" ")

#while문으로 접근
c=input()

n=ord(c)
i=ord('a')

while i<=n :
    print(chr(i), end=' ')
    i+=1