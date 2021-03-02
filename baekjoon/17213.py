#[과일 서리]- Silver 1
n=int(input())
m=int(input())
arr=[[-1]*(m+1) for _ in range(n+1)]

def count(n, m):
    if arr[n][m]!=-1:
        return arr[n][m]
    if n==1:
        arr[n][m]=1
        return 1
    cnt=0
    for i in range(1,m):
        cnt+=count(n-1,m-i)
    arr[n][m]=cnt
    return cnt
print(count(n, m))