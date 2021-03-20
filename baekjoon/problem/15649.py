#[N과 M(1)]- Silver 3
#1부터 N까지 자연수 중에서  M개를 고른 수열
import sys
n,m=map(int,sys.stdin.readline().split())
exit=[]

def solve():
    if len(exit)==m:
        print(' '.join(map(str,exit)))
        return
    for i in range(1,n+1):
        if i in exit:
            continue
        exit.append(i)
        solve()
        exit.pop()
solve()

#permutation을 이용해서 푼 풀이
from itertools import permutations
n,m=map(int,input().split())
per=permutations(range(1,n+1),m) 

for i in per:
    print(' '.join(map(str,i)))
    