#[N-Queen]- Gold 5
import sys
input=sys.stdin.readline

def queen(x):
    global ans
    if x>n:
        ans+=1
    else:
        for i in range(1,n+1):
            row[x]=i
            if right(x):
                queen(x+1)

def right(x):
    for i in range(1,x):
        if row[x]==row[i] or abs(row[x]-row[i])==x-i:
            return False
    return True

n=int(input())
row=[0 for _ in range(16)]
ans=0
queen(1)
print(ans)