N = int(input())
l = list(map(int, input().split()))
l.sort()
print(l[0])
#sort()와 sorted()잘 구분해서 사용
# sorted(iterable) -> 정렬된 iterable 객체를 반환
# sort() -> iterable 뒤에 붙어서 정렬해주는 함수