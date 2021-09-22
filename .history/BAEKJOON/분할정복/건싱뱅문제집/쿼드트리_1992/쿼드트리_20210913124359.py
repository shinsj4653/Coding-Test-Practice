n = int(input())
video = []
compressList = []

for i in range(n):
    video.append(input())

def isAllSame(n, x, y) :
    
    countNum = 0
    
    for i in range(n) :
        for j in range(n) :
            countNum += video[i][j]
            
    #All 0
    if countNum == 0 : 
    
    #All 1
    elif countNum == 1 :
        

# print(video)
def compress(n, x, y):

    num = isAllSame(n, x, y)
    

    if n >= 2:
        compress(n // 2, x, y)
        compress(n // 2, x, y + n // 2)
        compress(n // 2, x + n // 2, y)
        compress(n // 2, x + n // 2, y + n // 2)


compress(n, 0, 0)
