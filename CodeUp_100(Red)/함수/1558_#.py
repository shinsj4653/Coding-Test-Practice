#리스트요소들 순서 뒤집기 -> 리스트이름.reverse()
#문자열은 변경불가, 대신 슬라이싱 및 더하기 연산으로 가능
global n

def f(num) :
    ans = str(num)
    ans_list = []  
    i = 0
    
    real_ans = str()

    for ch in ans : 
        ans_list.append(ch)
    ans_list.reverse()

    for ch in ans_list :

        real_ans = real_ans + ch

    return real_ans


n = int(input())

print(f(n))