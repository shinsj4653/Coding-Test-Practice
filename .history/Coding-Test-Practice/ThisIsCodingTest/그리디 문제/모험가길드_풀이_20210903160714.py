#idea : 현재 그룹에 포함된 모험가 수가 현재 확인하고 있는 공포도 보다 크거나 같으면 이를 그룹으로 설정.
#문제에서 주어진 '공포도'랑 '사람 명수'를 활용하라는 것이 문제의도


n = int(input())
data = list(map(int, input().split()))
data.sort() #오름차순 정렬을 해야, 항상 최소한의 모험가의 수만 포함하여 그룹 결성.
# -> 최대한 많은 그룹이 구성되는 방법이므로, 항상 최적의 해 구하기 가능!

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가 수

for i in data :
    count += 1
    if count >= i : #이러면 그룹 결성
        result += 1
        count = 0

print(result)
