#[유기농 배추]- Silver 2
import sys
sys.setrecursionlimit(50000) #재귀 시간제한
cnt=0; arr=[]
dx=[-1,0,1,0]; dy=[0,1,0,-1]

def dfs(x,y):
    matrix[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        if matrix[nx][ny]==1:
            dfs(nx,ny)

def organic():
    cnt=0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==1:
                dfs(i,j)
                cnt+=1
    print(cnt)


t=int(input())
for i in range(t):
    m,n,k=map(int,sys.stdin.readline().split())
    matrix=[[0]*n for _ in range(m)]
    for _ in range(k):
        cabb=list(map(int,input().split()))
        matrix=[cabb[0]][cabb[1]]=1
    organic()



