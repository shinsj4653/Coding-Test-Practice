n = int(input())
sum = 0
num = 1

while sum < n :

    sum += num
    if sum >= n :
        break
    num = num + 1

print(num)

#문제에 과정이 있음.
#1, 2, 3 ..를 순서대로 계속 더해 -> num += 1이 먼저
#계속 더해 합을 만들어가다가 -> sum += num이 나중에

#풀이2
a=input()

n=int(a)

i=0
s=0
while s<n :
    i+=1
    s+=i

print(i)