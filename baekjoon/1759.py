#[암호 만들기]- Gold 5
import sys
from itertools import combinations

l,c=map(int, input().split())
pwd=list(map(str, input().split()))
pwd.sort()

alpha=['a','e','i','o','u']

com=combinations(pwd,l)
for i in com:
    cnt=0
    for j in i:
        if j in alpha:
            cnt+=1

    if cnt>=1 and cnt<=l-2:
        print(''.join(i))