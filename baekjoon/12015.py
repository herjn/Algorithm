#[가장 긴 증가하는 부분 수열2]- Gold 2
import bisect
n=int(input())
arr=list(map(int, input().split()))

dp=[arr[0]]
lens=len(dp)
for i in range(n):
    if arr[i]>dp[-1]:
        dp.append(arr[i])
    else:
        idx=bisect.bisect_left(dp, arr[i])
        dp[idx]=arr[i]
        
print(lens)