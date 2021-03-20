#[구간 합 구하기5]- Silver 1
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
table=[list(map(int,input().split())) for _ in range(n)]

for i in range(2):
    for j in range(n):
        if i==1 and j==0:
            continue
        for k in range(n):
            if i==0:
                if k==0:
                    continue
                table[j][k]=table[j][k-1]
            else:
                table[j][k]=table[j-1][k]

for i in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    if x1==1 and y1==1:
         print(table[x2-1][y2-1])
    elif x1==1:
        print(table[x2-1][y2-1]-table[x2-1][y1-2])
    elif y1==1:
        print(table[x2-1][y2-1]-table[x1-2][y2-1])
    else:
        print(table[x2-1][y2-1]-table[x2-1][y1-2]-table[x1-2][y2-1]+table[x1-2][y1-2])