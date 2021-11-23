# n, m = map(int, input().split())
# visited = [False] * (n + 1)
# visited[0] = True
# result = []
# loopCount = 0
# totalLoop = 1

# k_count = 0
# for k in range(n, 0, -1):
#     if k_count == m:
#         break
#     totalLoop *= k
#     k_count += 1
# i = 1

# while True:

#     if loopCount == totalLoop:
#         break

#     if len(result) == 0:
#         result.append(i)
#         visited[i] = True

#     for j in range(1, n + 1):

#         if len(result) == m:
#             break
#         else:
#             if visited[j] == True:
#                 continue
#             else:
#                 result.append(j)
#                 visited[j] = True

#     for r in result:
#         print(r, end=" ")
#     print()

#     if False not in visited:
#         result = []
#         for k in range(1, n + 1):
#             visited[k] = False
#         i += 1
#     else:
#         result.pop()

#     loopCount += 1

# 정석대로 푸는건 실패.. -> 파이썬의 순열 라이브러리 필요

# import itertools

# n, m = map(int, input().split())

# result = []
# for i in range(1, n + 1):
#     result.append(i)

# for x in itertools.permutations(result, m):
#     list(x)
#     for littleX in x:
#         print(littleX, end=" ")
#     print()

# 정석 풀이
n, m = map(int, input().split())

s = []


def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()

# 병현 풀이
n, m = map(int, input().split())
seq = [0] * m


def isValid(num, s):
    return False if num in s else True


def dfs(loc, num, seq):
    newseq = seq.copy()
    newseq[loc] = num
    if loc + 1 >= m:
        print(" ".join(map(str, s)))
    else:
        for i in range(1, n + 1):
            if isValid(1, newseq.copy()):
                dfs(loc + 1, 1, newseq.copy())


for i in range(1, n + 1):
    seq = [0] * m
    dfs(0, 1, seq.copy())
