#그림으로 그려서 점화식 구해보기
#왼쪽부터 i - 1까지 덮개로 이미 채워져있으면..혹은 i - 2 까지 채워져있으면.. 이렇게해서
#맨 뒤의 경우에만 생각해보기. 왜냐면 앞은 다 정해진값들 이므로.
n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 3

for i in range(3, n + 1) :

    d[i] = (d[n - 1] + 2 * d[n - 2]) % 796796

print(d[n])