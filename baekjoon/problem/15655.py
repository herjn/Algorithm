#[N과 M(6)]- Silver 3
# N개 자연수 중에서 같은 수 여러번 가능 M개를 고른 수열(오름차순)
import sys
n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
visited = [False]*n
exit=[]
l.sort()
def solve(dep,idx,n,m):
    if dep==m:
        print(' '.join(map(str,exit)))
        return

    for i in range(idx,n):
        if not visited[i]:
            visited[i]=True
            exit.append(l[i])
            solve(dep+1,i+1,n,m)
            exit.pop()
            visited[i]=False
solve(0,0,n,m)