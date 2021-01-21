f = input()
ans = format(float(f),".6f")#소수점 6째 자리까지 반올림
print(ans)
#round()함수는 반드시 round(실수) or round(실수, 정수)
#round()는 끝자리가 0이면 출력을 하지 않는다.
#format(3.141414,".2f") 형식사용