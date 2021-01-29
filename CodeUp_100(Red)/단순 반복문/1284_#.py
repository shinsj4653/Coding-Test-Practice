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

#풀이2
import math

n = int(input())
a = []
index = 0
sq = int(math.sqrt(float(n)))

for i in range(0, 30) :
    a.append(0)

for i in range(2, sq + 1) :
    while n % i == 0 :
        n /= i
        a[index] = i
        index += 1

if n != 1 :
    