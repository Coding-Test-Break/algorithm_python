import heapq
import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# N, M이 바뀌었길래 위치를 반대로 해줬다.
M, N = map(int, input().split())

graph = [[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
  input_str = list(str(input()))
  for j in range(M):
    graph[i][j] = input_str[j]


# 우선순위 큐를 이용해 풀이.
def bfs(start_x, start_y):
  q = list()
  heapq.heappush(q, (0, (start_x, start_y)))
  visited[start_x][start_y] = True

  while q:
    wall, (x, y) = heapq.heappop(q)
    if (x, y) == (N - 1, M - 1):
      return wall
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 벽에 닿는 노드는 벽을 1개 더 부숴야 하므로 벽의 개수대로 min heap을 구성하여 당장 벽을 가장 적게 부숴도 되는 노드 먼저 방문한.
      if (0 <= nx < N) and (0 <= ny < M) and not visited[nx][ny]:
        if graph[nx][ny] == '1':
          heapq.heappush(q, (wall + 1, (nx, ny)))
        else:
          heapq.heappush(q, (wall, (nx, ny)))
        visited[nx][ny] = True
  

print(bfs(0, 0))


  


