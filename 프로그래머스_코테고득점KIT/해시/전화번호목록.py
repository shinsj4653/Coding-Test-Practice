def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            
            #phone_book[i + 1]이 phone_book[i]에 포함되고 시작되는지 확인
            #str.startswith(str 혹은 tuple)
            return False

    return True

#해시 사용한 올바른 방법은 밑에

def solution(phone_book) :
    answer = True
    hash_map = {}
    for phone_number in phone_book :
        hash_map[phone_number] = 1
        
    print(hash_map)
        
    for phone_number in phone_book :
        temp = ""
        for number in phone_number :
            temp += number
            if temp in hash_map and temp != phone_number :
                #key 값중에 phone_number가 있는지 확인
                #temp != phone_number : 자기자신이랑 같을땐 아무의미없으니 카운트 X
                answer = False
                
    return answer
                

solution(["119", "97674223", "1195524421"])
