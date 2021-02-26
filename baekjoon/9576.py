#[책 나눠주기]- Gold 1
from collections import deque

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    book=[False]*(n+1)

    hope=[]
    for i in range(m):
        hope.append(list(map(int,input().split())))
        hope.sort(key=lambda x:x[1])

    can=0
    while hope:
        x,y=hope.pop(0)
        for i in range(x,y+1):
            if not book[i]:
                can+=1
                book[i]=True
                break

    print(can)