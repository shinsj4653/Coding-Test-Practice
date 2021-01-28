import math
import sys

def is_prime_number(n) :

	for i in range(2, int(math.sqrt(n)) + 1) :
		
		if n % i == 0 :
			return False
	return True

n = int(input())

if n == 1 :
    print("wrong number")
    sys.exit()

for i in range(2, n) :

    if is_prime_number(i) == True and is_prime_number(n // i) == True and i * (n // i) == n :
        print(i,n // i)
        sys.exit()
        
print("wrong number")




