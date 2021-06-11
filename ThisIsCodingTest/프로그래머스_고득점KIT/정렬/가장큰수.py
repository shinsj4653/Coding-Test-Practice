#미해결

def solution(numbers):
    numbers = list(map(str, numbers))
    
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))

print(solution([6, 2, 10]))

#str(int()) 의 이유 : 0000이면 int()로 0으로 바꾸고 다시 문자열로 바꿔서 출력해야하기 때문
#문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다. 물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다.