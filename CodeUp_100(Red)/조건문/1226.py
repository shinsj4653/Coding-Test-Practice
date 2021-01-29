l = list(map(int, input().split()))
juhee = list(map(int, input().split()))

count = 0
bonus = False

for i in range(6) :
    
    for j in range(6) :
        if l[i] == juhee[j] :
            count += 1

    if l[6] == juhee[i] :
            bonus = True


if count == 6 :
    print("1")
elif count == 5 and bonus == True : 
    print("2")
elif count == 5 and bonus == False :
    print("3")
elif count == 4 : 
    print("4")
elif count == 3 :
    print("5")
else : 
    print("0")
