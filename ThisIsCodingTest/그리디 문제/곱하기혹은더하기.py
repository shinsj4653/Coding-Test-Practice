num_string = input()
num_list = []

for num in num_string :
    num_list.append(int(num))

index = 0
total = 0
while index < len(num_string)  :

    if index == 0 :
        total = num_list[index]

    if index > 0 and (total == 0 or num_list[index] == 0) : #둘중 하나라도 0이면 더하기
        total += num_list[index]
    
    else :
        total *= num_list[index]
    
    index += 1

print(total)
