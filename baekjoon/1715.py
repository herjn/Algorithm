import sys
import heapq

n=int(input())
card=[]

for _ in range(n):
    heapq.heappush(card,int(sys.stdin.readline()))

if len(card)==1:
    print(0)
else:
    ans=0
    while len(card)>1:
        ret1=heapq.heappop(card) #제일 작은 카드
        ret2=heapq.heappop(card) #두번째로 작은 카드
        ans+=ret1+ret2
        heapq.heappush(card,ret1+ret2) #더한 카드 다시 넣어줌
    print(ans)