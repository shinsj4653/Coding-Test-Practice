#소수 판별 함수랑 순열 알고리즘 활용
from itertools import permutations
import math

def is_prime_number(x) :
    
    if x == 0 or x == 1 :
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1) :
        
        #if x % i == 0 or x == 1 or x == 0: 1과 0은 for문 안에도 못 들어옴
            return False
        
    return True

def solution(numbers):
    answer = 0
    li = set() #중복을 허용하지 않기위해
    
    for i in range(1, len(numbers) + 1) :
        result = list(permutations(numbers, i))
        
        for num in result :
            li.add(int("".join(num)))
        
    
    print(li)
    
    for num in li :
        if is_prime_number(num) == True :
            answer += 1
    
    
    return answer

print(solution("011"))