#[N과 M(11)]- Silver 2
# N개 자연수 중에서 같은 수 여러개 M개를 고른 수열 
import sys
n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
exit=[]
l.sort()

def solve(dep,n,m):
    if dep==m:
        print(' '.join(map(str,exit)))
        return
    over=0
    for i in range(n):
        if over!=l[i]:
            exit.append(l[i])
            over=l[i]
            solve(dep+1,n,m)
            exit.pop()
solve(0,n,m)