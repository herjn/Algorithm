#[연구소]
import sys
import copy
from  collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#바이러스 확산
def virus():
    global safe
    vboard=copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if vboard[i][j]==2:
                virus_list.append([i,j])
    
    while virus_list:
        x,y=virus_list.popleft()
        for i in range(4):
            ax=x+dx[i]
            ay=y+dy[i]
            if 0<=ax<n and 0<=ay<m:
                if vboard[ax][ay]==0:
                    vboard[ax][ay]=2
                    virus_list.append([ax,ay])
    cnt=0
    for x in vboard:
        cnt+=x.count(0)
    safe=max(safe,cnt)

#벽 선택
def set_wall(x):
    if x==3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                board[i][j]=1
                set_wall(x+1)
                board[i][j]=0

virus_list=deque()
n,m=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
safe=0
set_wall(0)
print(safe)
