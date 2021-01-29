#print(format(10,'X'))
Alpha = input()

for i in range(15) :
    result = format(int(Alpha, 16) * (i + 1),'X')
    if i + 1 >= 10 :
        print(Alpha+'*'+format(i+1, 'X')+'='+result)
    else :
        print(Alpha+'*'+str(i+1)+'='+result)