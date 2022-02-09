```python
from copy import deepcopy
import sys
from collections import deque

def dfs(i):
  visited[i] = True
  print(i, end= " ")
  while graph[i]:
    node = graph[i].popleft()
    if not visited[node]:
      dfs(node)

def bfs(i):
  q = deque()
  q.append(i)
  while q:
    node = q.popleft()
    if visited_b[node]:
      continue

    visited_b[node] = True
    print(node, end= " ")

    for i in graph_b[node]:
      q.append(i)


N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  if u not in graph[v]: graph[v].append(u)
  if v not in graph[u]: graph[u].append(v)

for i in range(len(graph)):
  sorted_list = sorted(graph[i])
  graph[i] = deque(sorted_list)

graph_b = deepcopy(graph)
visited_b = deepcopy(visited)

dfs(V)
print()
bfs(V)
```

- 생각해보니까 dfs 문제 풀 때는 굳이 `deque`를 쓰지 않고 for문으로 순회하는게 나았을 것 같다.

```python
def dfs(V):
  if visited[V]:
    return
  visited[V] = True
  print(V, end = " ")
  for node in graph[V]:
    dfs(node)
```

이런 식으로
