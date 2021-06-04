def find_parent(parent, x) :

    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b :
        parent[a] = b

    else :
        parent[b] = a

v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1) :
    parent[i] = i

for _ in range(e) :
    a, b, cost : map(int, input().split())
    #비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

edges.sort()
#간선을 비용순으로 정렬

for edge in edges :
    cost, a, b = edge
    #사이클이 발생하지 않을 경우에만 집합에 포함.
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost

print(result)