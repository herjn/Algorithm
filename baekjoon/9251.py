#LCS
import sys
a=sys.stdin.readline().strip().upper()
b=sys.stdin.readline().strip().upper()
len_a,len_b=len(a),len(b)

dp=[[0]*len_b for _ in range(len_a)]
for i in range(1,len_a):
    for j in range(1,len_b):
        if a[i]==b[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])

print(dp[-1[-1]])