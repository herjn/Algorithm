#[아기상어]-Gold 4
from collections import deque

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def shark(x,y):
    queue,visited=deque([x,y]),set([x,y])
    ans=0
    s_size=2
    time,s_eat=0,0
    eat_flag=False
    
    while queue:
        size=len(queue)
        queue=deque(sorted(queue))
        for _ in range(size):
            x,y=queue.popleft()
            if mat[x][y]!=0 and mat[x][y]<s_size:
                mat[x][y]=0
                s_eat+=1

                if s_eat==s_size:
                    s_size+=1
                    s_eat=0

                queue,visited=deque(),set([x,y])
                eat_flag=True
                ans=time 

            for ix,iy in zip(dx,dy):
                ax=x+ix
                ay=y+iy

                if ax>=0 and ax<n and ay>=0 and ay<n and (ax,ay) not in visited:
                    if mat[ax][ay]<=s_size:
                        queue.append((ax,ay))
                        visited.add((ax,ay))
            
            if eat_flag:
                eat_flag=False
                break

        time+=1
    return ans
 

n=int(input())
mat=[list(map(int,input().split())) for _ in range(n)]

sx,sy=0,0
for i in range(n):
    for j in range(n):
        if mat[i][j]==9:
            sx,sy=i,j
            mat[i][j]=0

print(shark(sx,sy))

