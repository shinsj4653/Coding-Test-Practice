def solution(bridge_length, weight, truck_weights):
    
    print(truck_weights)    
    bridge = []
    time = 0
    
    
    while True :
        
        
        if len(truck_weights) == 0 :
            #일단 다리를 건너거나, 다리에 있거나.
            while len(bridge) > 0 :
                bridge.pop(0)
                time += 1
            break
        
        if len(bridge) < bridge_length and sum(bridge) + truck_weights[0] < weight :
            w = truck_weights.pop(0)
            bridge.append(w)
            time += 1
            
        else :
            bridge.pop(0)
            time += 1
            
        
    
    return time

print(solution(2, 10, [7, 4, 5, 6]))

#첫 오류 : 6이 bridge에 있을 때
#해결 방법 : truck_weights 길이가 0일떄, bridge가 0일때까지 하나씩 뽑으면서 time늘리기
#다리 길이만큼 한칸씩 움직여야함.-> 어떻게 카운트하지??
#큐랑 길이를 같이 병행 못해서 못품..

#포기.. -> 밑 풀이 참고

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length
    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)
    return answer

#모두 0으로 찬 bridge(list), 빼고, 뒤에 다시 0집어넣으면 이동한것처럼 됨.

