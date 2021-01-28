N = int(input())
l = list(map(int, input().split()))

for i in range(N) : 
    print(l[i])

#input()은 무조건 문자열만 가능
#숫자 가지고 코딩 해야하면 int() 하는거 잊지말기!
#.index()함수는 요소의 index를 반환함. 요소를 반환하지 않음.
#인덱싱하려면 l[1] 이런식으로