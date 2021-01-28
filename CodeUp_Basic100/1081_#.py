n, m = map(int, input().split())
for i in range(n) :
    for j in range(m) :
        print(i+1,j+1)

#n, m = int(input().split())
#int() argument must be a string, a bytes-like object or a number, not 'list'
#위에 주석 처럼 하면 input().split()은 list형이므로 오류남.
#map함수를 사용해야함.