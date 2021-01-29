N = int(input())
sum = 0

for i in range(N) :
    i+=1
    sum+=i
    if(sum >= N) :
        print(sum)
        break

    