#[구간합 구하기4]-Silver 3
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
table=list(map(int,input().split()))
sum=[0]
for i in range(n):
    sum.append(sum[-1]+table[i])

for _ in range(m):
    x,y=map(int,input().split())
    if x==1:
        print(sum[y])
    else:
        print(sum[y]-sum[x-1])

