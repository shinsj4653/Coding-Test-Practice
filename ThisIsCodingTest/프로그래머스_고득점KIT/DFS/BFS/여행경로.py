# def travel_dfs(used, tickets, stack) :
    
#     if False not in used :#티켓 모두 사용했을시
#         answer.append(stack.pop()) #이렇게 해야 마지막 도착지점도 경로에 포함됨
#         return
        
#     place = stack.pop()
    
#     for i in range(len(tickets)) :
#         if tickets[i][0] == place and used[i] == False :
            
#             stack.append(tickets[i][1])
#             used[i] = True
#             answer.append(place)
#             travel_dfs(used, tickets, stack)
            
    

# def solution(tickets):
#     global answer
#     answer = []
    
#     tickets.sort()
    
#     stack = ["ICN"]
#     used = [False] * len(tickets)    
    
    
#     travel_dfs(used, tickets, stack)
    
#     return answer

#테케 1,2 번 넣으면 오류뜸...
#이런케이스 -> "ICN","AAA" / "ICN","BBB" / "BBB" -> "ICN"
#알파벳 순이라면 1번을 바로 골라야하는데, 그러면 AAA공항이후로 갈 곳이 없으므로, 2 -> 3 -> 1 로해야함.

def solution(tickets):
    
    tickets.sort(reverse = True)
    routes = dict()
    
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
            
    st = ['ICN']
    ans = []
    
    while st:
        top = st[-1]
        if top not in routes or len(routes[top]) == 0 :
            ans.append(st.pop())
        else:
            st.append(routes[top].pop())
    ans.reverse()
    
    return ans

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))

# 1. { 시작점 : [도착점], ... } 형태의 인접 리스트 그래프를 생성합니다.
# 2. ‘도착점’의 리스트를 정렬합니다. (알파벳 순서로)
# 3. DFS 알고리즘을 사용해 모든 점을 순회합니다. (스택이 빌때까지)

# - 스택에서 가장 위 데이터(top)를 가져옵니다.
# - 가져온 데이터(top)가 그래프에 없거나, 티켓을 모두 사용한 경우, path에 저장
# - 아니라면, 가져온 데이터(top)을 시작점으로 하는 도착점 데이터 중 가장 앞 데이터(알파벳순으로 선택해야하므로)를 가져와 stack에 저장
# 4. path를 역순으로 출력 !