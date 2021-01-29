#인덱싱 관점으로 접근
word = input()
for i in range(len(word)):
    print('\''+word[i]+'\'')

#풀이2
word = input()
for w in word:
    print("'"+w+"'")
#문자열에서 각 문자 접근할 때, 인덱싱 필요x