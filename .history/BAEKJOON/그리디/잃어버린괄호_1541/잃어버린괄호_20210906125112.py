question = input()
result = 0

# 뺄셈 기호 기준으로 나누기
subList = question.split("-")
print(subList)

#subList안에서 + 있는 것들 따로 더해서 분류
numList = []

for s in subList :
    if s.index("+") != -1 :
        