year, month, date = input().split('.')
year = year.zfill(4)
month = month.zfill(2)
date = date.zfill(2)
print(year+"."+month+"."+date)
#문자열 타입에서 원하는 개수만큼 0채우기 -> zfill() 사용
#zfill(2) -> 두 자리 공간 주어지고 오른쪽에 숫자채워짐
#그리고 남은 공간에는 0채워짐.
