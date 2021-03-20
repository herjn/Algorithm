#[절대값 힙]- Silver 1
import sys
import heapq

num=int(input())
heap=[]
for _ in range(num):
    n=int(sys.stdin.readline())
    if n!=0:
        heapq.heappush(heap,(abs(n),n))
    else:
        try: print(heapq.heappop(heap)[1])
        except: print(0)