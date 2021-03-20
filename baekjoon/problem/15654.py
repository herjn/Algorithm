#[N과 M(5)]- Silver 3
#N개 자연수 중에서 M개를 고른 수열 (중복x)
import sys
n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
visited = [False]*n
exit=[]
l.sort()
def solve(dep,n,m):
    if dep==m:
        print(' '.join(map(str,exit)))
        return

    for i in range(n):
        if not visited[i]:
            visited[i]=True
            exit.append(l[i])
            solve(dep+1,n,m)
            exit.pop()
            visited[i]=False
solve(0,n,m)