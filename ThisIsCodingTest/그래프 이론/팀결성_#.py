def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b


n, m = map(int, input().split())

parent = [0] * (n + 1)
graph = []

for i in range(n + 1) :
    parent[i] = i

for _ in range(m) :
    one_zero, a, b = map(int, input().split())
    #graph[one_zero].append((a, b))
    #이런식으로 복잡하게 x -> 그냥 바로 one_zero 값 0 or 1인지 확인하기!
    #굳이 리스트에 넣을 필요x
    graph.append((one_zero, a, b))
    

for g in graph :

    one_zero, a, b = g

    if one_zero == 0 : #union
        union_parent(parent, a, b)
    
    elif one_zero == 1 :
        if find_parent(parent, a) == find_parent(parent, b) :
            print("YES")
        else :
            print("NO")
    

