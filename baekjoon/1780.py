n=int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
one,zero,minus=0,0,0
def papernum(x,y,n):
    global one,zero,minus
    check=paper[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if(paper[i][j]!=check):
                for k in range(3):
                    for m in range(3):
                        papernum(x+k*n//3,y+m*n//3,n//3)
                return 
    if(check == -1):
        minus+=1
    elif(check == 0):
        zero+=1
    else:
        one+=1

papernum(0,0,n)
print(minus)
print(zero)
print(one)