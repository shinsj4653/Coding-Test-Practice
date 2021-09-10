#왼, 오 기준 판단이 힘듦!
#0, 즉 이미 'A'인 자리는 안 가도 됨.
#어떻게 해야 효울적??

def solution(name):
    answer = 0
    
    #13칸 움직여야하면 위가 이득
    #아니면 아래가 이득
    
    ch_list = []
    
    for ch in name :
        ch_list.append(ord(ch) - ord('A'))
    
    print(ch_list)
    
    for i in range(len(ch_list)) :
        if ch_list[i] > 13 :
            ch_list[i] = 26 - ch_list[i]
            
    #여기까지는 위, 아래 움직이는 횟수 모두 구함.
    
    #이제 왼, 오 횟수를 구해야함.
    #0의 개수, 즉 안 바꿔도 되는 칸의 개수를 기준으로
    
    #첫번째 위치 제외하고 나머지 원소개수 합 - 0 개수합    
    #-> 오류남.
    
    #3가지 방법
    #쭉 오른쪽, 쭉 왼쪽, 오른쪽 갔다가 왼쪽
    
    if ch_list[1:len(ch_list) // 2 + 1].count(0) == int(ch_list.count(0)) or ch_list[1:len(ch_list) // 2 + 1].count(0) == 0 : #첨부터 왼쪽 가는게 이득!(또는 오른쪽)
        
        answer = sum(ch_list) + len(ch_list) - 1 - ch_list[1:].count(0)
    
    elif ch_list[1] != 0  : #오 갔다가 왼            
        return answer
    
#알파벳 문제에서 특정 숫자를 사용하는 거 보단, min(), max()함수 사용해보기

def solution(name) :
    
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0
    answer = 0
    
    while True :
        answer += change[idx]
        change[idx] = 0
        if sum(change) == 0 :
            return answer
        
        #좌, 우 이동 방향을 정하기
        left, right = 1, 1
        while change[idx - left] == 0 : #change[-1] : 맨 뒤 -> 이 특성 활용!
            left += 1
        
        while change[idx + right] == 0:
            right += 1
            
        answer += left if left < right else right
        idx += -left if left < right else right