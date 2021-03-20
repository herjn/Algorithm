#[N과 M(12)]- Silver 2
# N개 자연수 중에서 같은 수 여러개 M개를 고른 수열(비내림차순)
import sys
n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
exit=[]
l.sort()

def solve(dep,idx,n,m):
    if dep==m:
        print(' '.join(map(str,exit)))
        return
    for i in range(idx,n):
            exit.append(l[i])
            solve(dep+1,i,n,m)
            exit.pop()
solve(0,0,n,m)