#[IOIOI]- Silver 2
import sys
input = sys.stdin.readline

n=int(input().rstrip())
m=int(input().rstrip())
s=input().rstrip()

answer=0; count=0
i=1
while i < m-1:
    if s[i-1] == "I" and s[i] == "O" and s[i+1] == "I":
        count+=1
        if count == n:
            count-=1
            answer+=1
        i+=1
    else:
        count=0
    i+=1
print(answer)