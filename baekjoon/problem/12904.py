#[A와 B]- Gold 5
import sys
input=sys.stdin.readline

s,t=[list(input().strip())for _ in range(2)]
while len(s)!=len(t):
    if t[-1]=='A':
        t.pop()
    else:
        t.pop()
        t=t[::-1] #역순
print(1 if s == t else 0)
