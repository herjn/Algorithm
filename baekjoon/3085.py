import sys
n=int(sys.stdin.readline())
mat=[list(map(str,input())) for _ in range(n)]

ans=0
def check(mat):
    cnt=0
    for i in range(n):
        row,col=1,1
        for j in range(n-1):
            if mat[i][j]==mat[i][j+1]:
                row+=1
            else:
                cnt=max(cnt,row)
                row=1
            if max[j][i]==mat[j+1][i]:
                col+=1
            else:
                cnt=max(cnt,col)
                col=1
        cnt=max(cnt,row,col)
    return cnt

for i in range(n):
    for j in range(n-1):
        if mat[i][j]!=mat[i][j+1]:
            res=mat[i][j]
            mat[i][j]=mat[i][j+1]
            mat[i][j+1]=res

            ans=max(ans,check(mat))
            res=mat[i][j]
            mat[i][j]=mat[i][j+1]
            mat[i][j+1]=res

        if  mat[j][i]!=mat[j+1][i]:
            res=mat[j][i]
            mat[j][i]=mat[j+1][i]
            mat[j+1][i]=res

            ans=max(ans,check(mat))
            res=mat[j][i]
            mat[j][i]=mat[j+1][i]
            mat[j+1][i]=res
print(ans)


