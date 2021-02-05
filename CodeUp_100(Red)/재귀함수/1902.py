import sys
def show_num(n) :
    if n == 0 :
        sys.exit()
    
    print(n)
    n -= 1
    show_num(n)

n = int(input())
show_num(n)