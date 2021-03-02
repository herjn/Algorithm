#[친구]- Silver 1
import sys
input=sys.stdin.readline
n=int(input())
visit=[[0] * n for i in range(n)]
arr=[]
def friend():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if arr[i][j]=="Y" or (arr[i][k]=="Y" and arr[k][j]=="Y"):
                    visit[i][j]=1

for i in range(n):
    arr.append(list(input()))
friend()
ans=0
for i in range(n):
    cnt=0
    for j in range(n):
        if visit[i][j]==1:
            cnt+=1
    ans=max(ans,cnt)
print(ans)