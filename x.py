import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
count = 0
max_visit = 0

for _ in range(N):
  graph.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs_stack(start_x, start_y):
  visit_count = 0
  stack = list()
  stack.append((start_x, start_y))

  while stack:
    x, y = stack.pop()
    if graph[x][y] == 1:
      graph[x][y] = -1 
      visit_count += 1
      
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > N - 1 or nx < 0 or ny > M - 1 or ny < 0:
          continue
        stack.append((nx, ny))

  return visit_count


for i in range(N):
  for j in range(M):
    if graph[i][j] == 1:
      max_visit = max(max_visit, dfs_stack(i, j))
      count += 1

print(count)
print(max_visit)