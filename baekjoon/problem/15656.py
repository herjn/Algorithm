#[N과 M(7)]- Silver 3
# N개 자연수 중에서 같은 수 여러번 가능 M개를 고른 수열
import sys
n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
exit=[]
l.sort()
def solve(dep,n,m):
    if dep==m:
        print(' '.join(map(str,exit)))
        return
    for i in range(n):
        exit.append(l[i])
        solve(dep+1,n,m)
        exit.pop()
solve(0,n,m)