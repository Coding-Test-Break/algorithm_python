import sys

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

def dfs(s, depth):
  if d[s] == 'INF' or d[s] > depth:
    d[s] = depth
    
    for node in graph[s]:
      dfs(node, d[s] + dist[u][v])
    

graph = [[] for _ in range(V + 1)]
dist = [[100 for _ in range(V + 1)] for _ in range(V + 1)]
d = ['INF' for _ in range(V + 1)]

for _ in range(E):
  u, v, w = map(int, sys.stdin.readline().split())
  dist[u][v] = min(dist[u][v], w)
  
  if v not in graph[u]:
    graph[u].append(v)


dfs(K, 0)

for i in range(1, V + 1):
  print(d[i], end= " ")