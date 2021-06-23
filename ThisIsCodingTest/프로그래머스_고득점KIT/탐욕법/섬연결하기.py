#그래프?? 접근을 어케해야하지..
def ancestor(node, parents):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)

def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer

#크루스칼 알고리즘 복습하기!
#그리디 알고리즘으로 분류됨.

#하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
#-> 신장트리
#신장트리중, 최소 비용으로 만들 수 있는 신장 트리를 찾는알고리즘 : 최소 신장 트리 알고리즘

#연결할 수 없는 섬은 주어지지 않는다 -> 크루스칼 알고리즘!

#핵심 원리 : 가장 거리가 짧은 간선부터 차례대로 집합에 추가!
#사이클이 발생되면 제외!

