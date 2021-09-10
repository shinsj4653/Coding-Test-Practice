question = input()
result = 0

# 뺄셈 기호 기준으로 나누기
subList = question.split("-")
# print(subList)

# subList안에서 + 있는 것들 따로 더해서 분류
numList = []

# isFirstNegative 변수 추가
isFirstNegative = False

for s in subList:

    if s == "":  # 처음 변수가 음수임.
        isFirstNegative = True

    elif "+" in s:
        # a, b = s.split('+')
        # sum = int(a) + int(b)
        # numList.append(-sum)

        # 위와 같이 하면, +50+50+50은 에러가 남.

        numList.append(sum(list(map(int, s.split("+")))) * -1)
    else:
        numList.append(-int(s))

if isFirstNegative == False:
    numList[0] *= -1

print(sum(numList))
