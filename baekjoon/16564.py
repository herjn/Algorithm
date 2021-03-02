#[히오스 프로게이머]- Silver 1
import sys
input=sys.stdin.readline

n,k=map(int, input().split())
arr=sorted([int(input()) for _ in range(n)])
team_level=arr[0]; i=0

while k:
    level_up = arr[i+1]-team_level
    if k>= level_up * (i+1):
        k-=level_up * (i+1)
        team_level+=level_up
    else:
        team_level+=k//(i+1)
        k=0
    i+=1
print(team_level)
