n,m,v=map(int,input().split())
matrix=[[0]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    x,y=map(int,input().split())
    matrix[x][y]=matrix[y][x]=1

def dfs(v):
    visited[v]=True
    print(v, end=' ')
    for i in range(1,n+1):
        if matrix[v][i]==1 and not visited[i]:
            dfs(i)

def bfs(v):
    queue=[v]
    visited[v]=False
    while queue:
        v=queue.pop(0)
        print(v,end=' ')
        for i in range(1,n+1):
            if matrix[v][i]==1 and visited[i]:
                queue.append(i)
                visited[i]=False

dfs(v)
print()
bfs(v)