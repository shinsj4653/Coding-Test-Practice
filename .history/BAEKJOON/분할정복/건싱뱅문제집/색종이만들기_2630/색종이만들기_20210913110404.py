n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

# print(paper)
x = 0 #가로
y = 0 #세로

white = 0
blue = 0

def searchPaper(n, x, y, paper) {
    
    initial = paper[x][y]
    
    if n == 1 :
        if initial == 0 :
            white += 1
        else:
            blue += 1
    
    elif n >= 2 :
        for i in range(n) :
            for j in range(n) :
                if initial != paper[i][j] :
                    n //= 2
                    searchPaper(n, x, y, paper)
                    searchPaper(n, x, y + n, paper)
                    searchPaper(n, x + n, y, paper)
                    searchPaper(n, x + n, y + n, paper)
    

}
