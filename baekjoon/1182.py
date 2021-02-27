#[부분 수열의 합]- Silver2

import sys
input=sys.stdin.readline

def dfs(idx,sum):
    global cnt
    if idx >= n:
        return
    sum+=lst[idx]
    if sum==s:
        cnt+=1

    dfs(idx+1, sum-lst[idx])
    dfs(idx+1, sum)

cnt=0
n,s=map(int, input().split())
lst=list(map(int, input().split()))

dfs(0, 0)
print(cnt)