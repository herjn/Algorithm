#[스타트와 링크]- Silver 3

#dfs로 풀기
import sys
input=sys.stdin.readline

def dfs(idx, cnt):
    global ans
    if cnt==n // 2:
        start,link=0,0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += a[i][j]
                elif not select[i] and not select[j]:
                    link += a[i][j]
        ans = min(ans, abs(start-link))

    for i in range(idx, n):
        if select[i]: #값이 있으면 패스
            continue
        select[i] = 1 #값이 없으면 1로 채워줌
        dfs(i+1, cnt+1)
        select[i] = 0

n= int(input())
select=[0 for _ in range(n)]

a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))

ans = sys.maxsize
dfs(0,0)
print(ans)

