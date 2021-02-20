#A를 B로!
from collections import deque
a,b=map(int,input().split())
ans=-1
q=deque([(a,1)])

while q:
    c,cnt=q.popleft()
    if c==b:
        ans=cnt
        break
    if b>=c*2:
        q.append((c*2,cnt+1))
    if b>=int(str(c)+'1'):
        q.append((int(str(c)+'1'),cnt+1))

print(ans)
