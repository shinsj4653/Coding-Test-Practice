question = input()
result = 0

# 뺄셈 기호 기준으로 나누기
subList = question.split("-")
print(subList)

# subList안에서 + 있는 것들 따로 더해서 분류
numList = []

for s in subList:
    index = 0

    if len(s) >= 3:
        a, b = s.split("+")
        sum = -(int(a) + int(b))
        numList.append(sum)
        index += 1

    else:
        if len(s) == 0:
            index += 1
            continue
        else:
            if index == 0:
                index += 1
                numList.append(int(s))

            else:
                index += 1
                numList.append(-int(s))


for n in numList:
    result += n

print(result)
