#[DFS와 BFS]- Silver 1

#1.인접행렬로 그래프 구현
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


#2.인접리스트로 그래프 구현
import sys 
from collections import deque 

def dfs(graph, v):
    visited = []
    stack = [v]
    while stack:
        n = stack.pop() 
        if n not in visited:
            visited.append(n)
            stack += reversed(graph[n])
            return visited

def bfs(graph, v):
    visited = []
    queue = deque([v])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n]
            return visited

input = sys.stdin.readline            
n,m,v = map(int,input().split())
graph = {i:[] for i in range(1,n+1)}

for i in range(1, m+1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for key in graph:
    graph[key].sort()

print(' '.join(list(map(str,dfs(graph, v)))))
print(' '.join(list(map(str,bfs(graph, v)))))
