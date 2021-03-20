#[N과 M(4)]- Silver 3
#1부터 N까지 자연수 중에서 같은 수 가능 M개를 고른 수열 (비내림차순)
import sys
n,m=map(int,sys.stdin.readline().split())
exit=[]

def solve(dep,idx,n,m):
    if dep==m:
        print(' '.join(map(str,exit)))
        return
    for i in range(idx,n):
        exit.append(i+1)
        solve(dep+1,i,n,m)
        exit.pop()
solve(0,0,n,m)