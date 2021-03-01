#[제곱ㄴㄴ수]- Gold1 
import math

def solve():
    min,max=map(int,input().split(' '))
    num=[True]*(max-min+1)
    n=1; cnt=0

    while n*n<=max:
        n+=1
        square=n*n
        a=min//square

        while square*a<=max:
            i=square*a-min
            
            if i>=0 and num[i]:
                cnt+=1
                num[i]=False
            a+=1
    print(len(num)-cnt)

solve()