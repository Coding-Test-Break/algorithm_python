import sys
from collections import deque

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

node = [[] for _ in range(N + 1)]

for _ in range(M):
  x, y = map(int, sys.stdin.readline().split())
  node[x].append(y)
  node[y].append(x)

visited = [0 for i in range(N + 1)]
visited[1] = 1
def bfs(s):
  q = deque(s)
  count = 0
  while q:
    x = q.popleft()
    for i in node[x]:
      if not visited[i]:
        q.append(i)
        visited[i] = 1
        count += 1
  return count

print(bfs([1]))