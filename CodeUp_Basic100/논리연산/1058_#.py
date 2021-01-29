a, b = input().split()
n1 = int(a)
n2 = int(b)
print(int(not(n1 | n2)))
#모두 거짓일 때에만 참 -> 모두 거짓일때 거짓인 or연산 을 not 으로 해버리면됨.
#말을 수식으로 표현 : not a & not b
#not(a | b) 이렇게 표현 가능.
