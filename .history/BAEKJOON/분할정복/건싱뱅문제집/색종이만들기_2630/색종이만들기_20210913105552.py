n = int(input())
paper = []

for i in range(n):
    paper.append(list(map(int, input().split())))

# print(paper)
x = 0 #가로
y = 0 #세로
def searchPaper(n, x, y, paper) {
    
    initial = paper[x][y]
    
    for i in range(n) :
        for j in range(n) :
            if initial != paper[i][j] :
                n //= 2
                searchPaper(n, )
    

}
