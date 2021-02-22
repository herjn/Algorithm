#[트리의 부모 찾기]- Silver 2
import sys

node=int(input())
graph=[[] for _ in range(node+1)]
parent=[[] for _ in range(node+1)]

#트리를 그래프 형태로 생성
for _ in range(node-1):
    i,j=map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

def dfs(graph_list, start, parent):
    stack = [start]
    while stack:
        node = stack.pop()
        for i in graph_list[node]:
            parent[i].append(node)
            stack.append(i)
            graph_list[i].remove(node)
    return parent

for i in list(dfs(graph, 1, parent))[2:]:
    print(i[0])