#첫날은 문제 푸는걸로 취급x
#True: 대문자 주의
a, b, c = map(int, input().split())
day=1
#print(day % (a + 1) != 0) -> True를 반환함. 1을 반환하지 않음.
while(day % a!=0 or day % b!=0 or day % c!=0) : 
    
    day+=1 
print(day)

#not으로 다 묶고 & 을 | 로 변환 가능.
#&, | -> 1, 0 혹은 수를 다룰때 사용
#True 일때는 or, and 이렇게 영어로 작성해야!

#최소공배수 -> 그 수에 나눠지면 0 : 0은 프로그램 상 False인데, 이 문제에선 0을 True로 간주해야하므로 or 연산자이용
#모두 0이어야 참 -> or
#day % a가 0일때보다 0이 아닐때가 훨씬 많음 -> 따라서, 0이 아닐때를 이용하는게 더 편안.
#나머지가 0일때 '만' 거짓이므로, 이걸 기준으로 쓰기.

#최소공배수 -> 모든요소의 곱 / 최대공약수


