#N과 M 시리즈 (1) -15649

#permutation을 이용해서 푼 풀이
from itertools import permutations

n,m=map(int,input().split())
per=permutations(range(1,n+1),m) #tuple

for i in per:
    print(' '.join(map(str,i))) #tuple->str
    

#함수호출 이용해서 푼 풀이
n,m=map(int,input().split())
num=[]
def fact():
    if len(num)==m:
        print(' '.join(map(str,num)))
        return
    
    for i in range(1,n+1):
        if i in num:
            continue
        num.append(i)
        fact()
        num.pop()

fact()