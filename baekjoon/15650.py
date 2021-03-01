#[N과M(2)]- Silver 3
#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열 (오름차순)
import sys
n,m=map(int,sys.stdin.readline().split())
visited=[False] * n
exit=[]

def solve(dep,idx,n,m):
    if dep==m:
        print(' '.join(map(str,exit)))
        return
    
    for i in range(idx,n):
        if not visited[i]:
            visited[i]=True
            exit.append(i+1)
            solve(dep+1,i+1,n,m)
            visited[i]=False
            exit.pop()
solve(0,0,n.m)


#itertools이용 풀이
from itertools import combinations
n,m=map(int, input().split())
c=combinations(range(1,n+1),m)
for i in c:
    print(' '.join(map(str,i))) 