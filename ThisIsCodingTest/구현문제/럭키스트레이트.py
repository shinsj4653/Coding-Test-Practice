power = input()
power_len = len(power) // 2

i = 0
first = 0
second = 0

for num in power :
    
    if i < power_len :
        first += int(num)

    
    else :
        second += int(num)

    
    i += 1

if first == second :
    print("LUCKY")

else :
    print("READY")