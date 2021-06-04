def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])#경로 압축방법을 활용함.
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b : #b가 a의 부모
        parent[a] = b
    
    else :
        parent[b] = a

v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1) :
    parent[i] = i

for i in range(e) :
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합 : ', end = '')
for i in range(1, v + 1) :
    print(find_parent(parent, i), end = ' ')

print()

print('부모 테이블 : ', end = '')
for i in range(1, v + 1) :
    print(parent[i], end = ' ')

    