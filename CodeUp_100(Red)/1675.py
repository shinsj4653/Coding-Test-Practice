code = input()

for c in code : 

    if c == 'a' or c == 'b' or c =='c':
        print(chr(ord(c) + 23), end = '')

    elif c == ' ' :
        print(' ', end ='')

    else :
        print(chr(ord(c) - 3), end = '')

