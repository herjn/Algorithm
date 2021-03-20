#[N과 M(10)]- Silver 2
# N개 자연수 중에서 M개를 고른 수열 (비내림차순)
import sys
n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
exit=[]; visited = [False]*n
l.sort()

def solve(dep,idx,n,m):
    if dep==m:
        print(' '.join(map(str,exit)))
        return
    over=0
    for i in range(idx,n):
        if not visited[i] and over!=l[i]:
            visited[i]=True
            exit.append(l[i])
            over=l[i]
            solve(dep+1,i+1,n,m)
            visited[i]=False
            exit.pop()
solve(0,0,n,m)