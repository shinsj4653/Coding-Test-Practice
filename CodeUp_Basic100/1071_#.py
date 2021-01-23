#프로그램 강제종료
import sys

l = []

l = list(map(int,input().split()))

for i in l :
    
    if int(i) == 0 :
        sys.exit()

    print(i) 
    
    