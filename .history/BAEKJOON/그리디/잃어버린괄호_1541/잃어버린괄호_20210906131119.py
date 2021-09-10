question = input()
result = 0

# 뺄셈 기호 기준으로 나누기
subList = question.split("-")
print(subList)

# subList안에서 + 있는 것들 따로 더해서 분류
numList = []
index = 0

for s in subList:

    if len(s) >= 3:
        a, b = s.split("+")
        sum = -(int(a) + int(b))
        numList.append(sum)
        sum = 0

    else:
        if len(s) == 0:
            index += 1
            continue
        else:
            if index == 0:
                numList.append(int(s))

            else:
                numList.append(-int(s))
    index += 1


for n in numList:
    result += n

print(result)
