import sys
max=sys.maxsize

n,m=int(sys.stdin.readline),int(sys.stdin.readline)
travel=[list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if j==k:
                travel[j][k]=1
            if travel[j][i] and travel[i][k]:
                travel[j][k]=1

num=list(map(int, input().split()))
size=len(num)
for i in range(size-1):
    if travel[num[i]-1][num[i+1]-1]!=i:
        print("NO")
        sys.exit()
print("YES")