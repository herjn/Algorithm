import sys
d,k=map(int, sys.stdin.readline().split())
pre,curr=0,1
pre2,curr2=1,1

i=3
while i!=d:
    pre,curr=curr,pre
    curr+=pre
    pre2,curr2=curr2,pre2
    curr2+=pre2
    i+=1

i=1
state=False
while True:
    j=1
    while True:
        check=curr*i+curr2*j
        if check>k:
            break
        elif check==k:
            state=True
            break
        j+=1
    if state:
        break
    i+=1

print(i)
print(j)