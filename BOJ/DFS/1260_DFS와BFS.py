import sys

N, M, V = map(int, sys.stdin.readline().split())

graph = dict()
visited = [True] + [False for _ in range(N)]
for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# def dfs(graph, V):
    
    