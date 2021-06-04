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

n, m = map(int, input().split())

parent = [0] * (n + 1)

for i in range(1, n + 1) :
    parent[i] = i

edges = []
cost_array = []
result = 0

for i in range(m) :
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()#이러면 마지막 edge의 비용이 가장 큼.

for edge in edges :
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        cost_array.append(cost)

cost_array.sort(reverse=True)

for i in range(1, len(cost_array)) :
    result += cost_array[i]

print(result)