from collections import Counter

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    print(answer)
    
    return list(answer.keys())[0]

solution(["leo", "kiki", "eden"], ["eden", "kiki"])

#데이터 개수 셀때 유용한 collections 모듈의 Counter클래스
#- from collections import Counter

#개수가 0개 인거는 Counter클래스에 안뜸!

#Counter('hello world') 
#→ Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
#문자열에서 어떤 알파벳의 횟수가 가장 많은지 파악하려면 most_common()함수도 사용가능

#Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

#Counter('hello world').most_common(1) # [('l', 3)] #가장 개수가 많은 1개 데아터를 리턴.