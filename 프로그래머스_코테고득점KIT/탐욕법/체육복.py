#이 문제에서 어떻게 탐욕적으로 생각하지??
#-> 왼쪽요소부터탐색하여야함.
#오른쪽 부터 하면 빌려 받을 수 있는 학생들이 못 받는경우가 발생할 수 있음.

def solution(n, lost, reserve):
    answer = 0
    
    #reserve : 체육복을 빌려줄 수 있는 학생들 배열
    lost.sort()
    reserve.sort()
    
    students = [True] * (n + 1)
    
    for i in lost :
        if i in reserve :
            reserve.remove(i)
        
        else :
            students[i] = False
            
    for s in students :
        if s == False :
            idx = students.index(s)
            
            if idx - 1 in reserve or idx + 1 in reserve :
                if idx - 1 in reserve :
                    reserve.remove(idx - 1)
                  #한번 빌렸으면 끝!
                  #reserve에서 없애야!
                    
                elif idx + 1 in reserve :
                    reserve.remove(idx + 1)
                    
                students[idx] = True
                
    
    for i in range(1, n + 1) :
        if students[i] == True :
            answer += 1
        
    
    
    
    return answer

#인터넷 풀이
def solution(n, lost, reserve):
    answer = 0
    
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    #중복되는 번호가 없다 : set으로!
    #여벌 체육복 갖고 있는 학생이 도난 맞으면 못 빌려줌
    #reserve원소 중 lost에 있으면 reserve에서 빼야함!
    
    for i in set_reserve :
        if i - 1 in set_lost : #왼쪽부터 -> 그리디 사고법
            set_lost.remove(i - 1)
        
        elif i + 1 in set_lost :
            set_lost.remove(i + 1)
        
        
    
    
    
    return n - len(set_lost) #n을 괜히 준게아님! n에서 lost를 빼면 수업듣기가능한 학생들 나옴!