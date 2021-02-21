import sys
from collections import deque

def find():
    while q:
        place=q.popleft()
        if place==k:
            return visit[place]
        pos(place-1,place)
        pos(place+1,place)
        pos(place*2,place)

def pos(next,place):
    if maxsize>=next>=0 and (visit[next]==0 or visit[place]+1<visit[next]):
        q.append(next)
        visit[next]=visit[place]+1


if __name__=="__main__":
    n,k=map(int,input().split())
    maxsize=100001
    q=deque([n])
    visit=[0]*maxsize
    print(find())
