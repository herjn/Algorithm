#[1,2,3 더하기 2]- Silver 1
from sys import stdin

def plus(idx,sum,check):
    global cnt
    if sum>n:
        return
    
    if sum==n:
        cnt+=1
        if cnt==k:
            print(''.join(check)[:-1])
            exit(0)

    for i in range(1,4):
        check.append(str(i)+'+')
        plus(idx+1,sum+i,check)
        check.pop()

if __name__=="__main__":
    n,k=map(int,input().split())
    cnt=0
    plus(0,0,[])
    print(-1)

