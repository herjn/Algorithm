#[Z]-Silver 1
import sys
ans=0
def solve(n,x,y):
    global ans
    if x==r and y==c:
        print(int(ans))
        exit(0)
    
    if n==1:
        ans += 1
        return
    
    if not(x<=r<x+n and y<=c<y+n):
        ans += n*n
        return

    solve(n/2,x,y)
    solve(n/2,x,y+n/2)
    solve(n/2,x+n/2,y)
    solve(n/2,x+n/2,y+n/2)

n,r,c = map(int,sys.stdin.readline().split(' '))
solve(2**n,0,0)