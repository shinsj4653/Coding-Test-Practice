#37 11 답이 오류남.
import math
global a, n


a, n = map(int, input().split())
print(int(format(math.pow(a, n),".0f")))