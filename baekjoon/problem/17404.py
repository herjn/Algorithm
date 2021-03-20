#[RGB거리 2]- Gold 4
import sys
n=int(input())
color=[]
for _ in range(n):
    color.append([int(i) for i in sys.stdin.readline().split()])
 
ans=1001*1001
for x in range(3): 
    dp = [[0 for _ in range(n)] for _ in range(3)]
    for i in range(3): 
        if i==x:
            dp[i][0]=color[0][i]
            continue
        dp[i][0]=1001*1001
 
    for i in range(1,n): 
        dp[0][i]=color[i][0]+min(dp[1][i-1],dp[2][i-1])
        dp[1][i]=color[i][1]+min(dp[0][i-1],dp[2][i-1])
        dp[2][i]=color[i][2]+min(dp[0][i-1],dp[1][i-1])
    
    for k in range(3): 
        if k==x:
            continue
        ans=min(ans,dp[k][-1])
print(ans)