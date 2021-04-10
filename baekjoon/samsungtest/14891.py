#[톱니바퀴]
import sys
from collections import deque

def check_left(start, dirs):
    if start < 1 or tob[start][2] == tob[start+1][6]:
        return
    
    # 왼쪽 확인
    if tob[start+1][6] != tob[start][2]:
        check_left(start - 1, -dirs)
        tob[start].rotate(dirs)

def check_right(start, dirs):
    if start > 4 or tob[start-1][2] == tob[start][6]:
        return

    # 오른쪽 확인
    if tob[start-1][2] != tob[start][6]:
        # 인접한 톱니바퀴가 회전 가능한지부터 먼저 파악한다.
        check_right(start + 1, -dirs)
        tob[start].rotate(dirs)

        
    
# 기준 톱니바퀴가 있을 때, 왼쪽과 맞닿는 지점은 idx 2, 오른쪽은 6이다.
tob = {}
for i in range(1, 5):
    tob[i] = deque(list(map(int, list(sys.stdin.readline().replace("\n","")))))
n = int(sys.stdin.readline())

for _ in range(n):
    num, dirs = map(int, sys.stdin.readline().split())
    check_left(num-1, -dirs)
    check_right(num+1, -dirs)
    # 기준 톱니바퀴를 회전시킨다.
    tob[num].rotate(dirs)
    
ans=0
for i in range(4):
    ans += (2**i) * tob[i+1][0]
print(ans)
