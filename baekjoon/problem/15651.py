#[N과 M(3)]- Silver 3
#1부터 N까지 자연수 중에서 같은 수 여러번 가능 M개를 고른 수열
import sys
n,m=map(int,sys.stdin.readline().split())
exit=[]

def solve(dep,n,m):
    if dep==m:
        print(' '.join(map(str,exit)))
        return
    for i in range(n):
        exit.append(i+1)
        solve(dep+1,n,m)
        exit.pop()
solve(0,n,m)