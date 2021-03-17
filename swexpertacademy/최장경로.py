def dfs(idx,ans):
    global answer
    visited[idx]=0
    ans+=1
    if answer < ans:
        answer = ans
    for i in graph[idx]:
        if visited[i]:
            dfs(i,ans)
    visited[idx]=1


       
T = int(input())
for test in range(1, T+1):
    N , M = map(int,input().split())
    visited = [1 for i in range(N+1)]
    res = [list(map(int,input().split())) for _ in range(M)]
    graph = [[] for _ in range(N+1)]
    answer = 0
    for a,b in res:
        graph[a].append(b)
        graph[b].append(a)
    for i in range(N):
        dfs(i,0)

    print('#{} {}'.format(test, answer))