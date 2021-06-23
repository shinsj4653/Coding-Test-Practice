# def solution(routes):
#     answer = 0
#     routes.sort(key = lambda x:x[1])
#     checked = [False] * len(routes)
    
#     for i in range(len(routes)) :
#         if checked[i] == False :
#             camera = routes[i][1] #진출 지점에 카메라를 갱신
#             answer += 1
        
#         for j in range(i + 1, len(routes)) :
#             if routes[j][0] <= camera <= routes[j][1] and checked[j] == False :
#                 checked[j] = True
    
    
#     return answer

# print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]	))


#또다른 풀이

def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]	))