import sys
def print_num(i) :
    if i >= n :
        print(i)
        sys.exit()

    print(i)
    i += 1
    print_num(i)
    


global n
global i
i = 1
n = int(input())

print(print_num(i))

