#리스트 안에 튜플이 원소로 들어가 있을 때 정렬 방법
#이 문제에선 사전사용. 사전도 정렬가능!
#sorted() 함수는 list를 반환
#items()는 key, value둘다 가짐.

n = int(input())
l = dict()
for i in range(n) :
    a, b = input().split()
    l[int(b)] = a
ans = sorted(l.keys(), reverse = True)

print(l[ans[2]])
