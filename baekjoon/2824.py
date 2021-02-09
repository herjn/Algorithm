import sys
from sys import stdin

def gcd(a, b):
    while b>0:
        a,b=b,a%b
    return a

_ = stdin.readline()
arr=list(map(int, stdin.readline().split()))
A=1

for num_a in arr:
    A*=num_a

_=stdin.readline()
arr2=list(map(int, stdin.readline().split()))
B=1

for num_b in arr2:
    B*=num_b

ans=str(gcd(A,B))
print(ans[-9:])