#가장 큰 증가 부분 수열4
n=int(input())
long=list(map(int,input().split()))

dp=[1 for _ in range(n)]
arr=[[i] for i in long]

for i in range(n):
    for j in range(i):
        if long[i]>long[j]:
            if dp[j]+1>dp[i]:
                arr[i]=arr[j]+[long[i]]
                dp[i]=dp[j]+1
len,flag=0,0
for i in range(n):
    if len<dp[i]:
        len=dp[i]
        flag=i

print(len)
print(*arr[flag])