#index() 함수 사용법 : 리스트이름.index(리스트요소)
#for key in key_list : 사전의 키만 뽑은 리스트에서 키 탐색

N = int(input())
l = list(map(int, input().split()))

ans = dict()

l_new = sorted(l)

ans_list = []


for i in range(N) : 
    ans[l_new[i]] = l_new.index(l_new[i]) 

key_list = ans.keys()

for i in range(N) :
    for key in key_list :
        if l[i] == key :
            ans_list.append(ans[key])


for i in range(N) :
    print(ans_list[i], end = " ")