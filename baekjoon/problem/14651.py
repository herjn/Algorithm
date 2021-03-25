# -*- coding: utf-8 -*-
#[걷다보니 신척역 삼]- Silver 1

n=int(input())
dp=[[0]*3 for _ in range(n)]
dp[0][0]=0
dp[0][1]=1
dp[0][2]=1

for i in range(1,n):
    for j in range(3):
        dp[i][j]=int((dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%(1e9+9))
print(dp[n-1][0])