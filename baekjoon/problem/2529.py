#[부등호]- Silver 2

num=int(input())
op=input().split()
check=[False]*10
max,min= "",""

#부등호 조건이 만족할때만
def oper(i,j,k):
    if k==">":
        return i>j
    else:
        return i<j

def solve(cnt,ss):
    global max,min
    if cnt>num:
        if len(min)==0: min=ss
        else: max=ss

    for i in range(10): 
        if check[i]==False:
            if cnt==0 or oper(ss[-1],str(i),op[cnt-1]):
                check=True
                solve(cnt+1,ss+str(i))
                check=False
solve(0,"")
print(max)
print(min)