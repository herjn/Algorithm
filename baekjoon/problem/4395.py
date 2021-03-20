#[Steps]- Silver 1
import sys
import math

def fact(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a

def solution():
    n=int(sys.stdin.readline()) 
    for _ in range(n):
        x,y=map(int,input().split(' '))
        distance=y-x
        i=1
        while i*i<distance:
            i+=1
        if distance<(i*i)-i+1:
            print(2*i-2)
        else:
            print(2*i-1)
solution()