a, b, c = input().split()
n1 = int(a)
n2 = int(b)
n3 = int(c)

print(n1 > n2 and (n2 > n3 and n3 or n2) or (n1 > n3 and n3 or n1))