string = input()
new_list = []
num = 0


for c in string :
    if ord(c) >= 65 : #숫자가 아닌 문자 일때만 
        new_list.append(ord(c))
    else :
        num += int(c)

new_list.sort()

for n in new_list :
    print(chr(n), end = "")

print(num, end = "")
