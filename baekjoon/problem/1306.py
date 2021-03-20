#[달려라 홍준]- Platinum 5
import sys

n,m = list(map(int, input().split()))
light = list(map(int, sys.stdin.readline().split()))

board = max(light[:2*m-1])
print(board,end=" ")

for i in range(m, n-m+1):
    if(board < light[i+m-1]):
        board = light[i+m-1]

    else:
        if(board == light[i-m]):
            board = max(light[i-m+1:i+m])

    print(board,end=" ") #광고판 세기 