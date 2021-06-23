def solution(money):
    #개미털기랑 똑같!
    answer = 0
    DP = [0] * len(money)
    
    DP[0] = money[0]
    DP[1] = money[1]
    
    for i in range(2, len(money)) :
        DP[i] = max(DP[i - 1], money[i] + DP[i - 2])
        
        if i == len(money) - 1 :
            DP[i] = max(money[i - 1] + DP[0], money[i] + DP[i - 2])
    
    answer = max(DP)    
    
    return answer

#45점짜리..왜??
def solution(money):
    #개미털기랑 똑같!
    answer = 0
    DP = [0] * len(money)
    
    DP[0] = money[0]
    DP[1] = max(money[0], money[1])
    
    for i in range(2, len(money) - 1) :#첫집을 무조건 터는 경우
        DP[i] = max(DP[i - 1], money[i] + DP[i - 2])
    
    DP2 = [0] * len(money)
    DP2[0] = 0
    DP2[1] = money[1]
    
    for i in range(2, len(money)) : #마지막 집을 무조건 터는 경우
        DP2[i] = max(DP2[i - 1], money[i] + DP2[i - 2])
    
    answer = max(max(DP), max(DP2))    
    
    return answer

#첫집, 마지막 집 터는 경우로 2가지로 나눠서 생각해야함.