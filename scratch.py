from collections import deque
import sys


N, K = map(int, sys.stdin.readline().split())

# N -> K 까지의 최단거리를 저장하는 list
dp = [False for _ in range(100001)]
dp[N] = 0

def bfs():
  # (node, 최단거리)를 저장하는 큐
  q = deque()
  q.append((N, 0))
  
  while q:
    node, dist = q.popleft()

    # node가 허용된 index안에 있고, 한번도 방문하지 않은 node이거나 방문했지만 최단거리가 비효율적인 경우 큐에 추가
    for i, j in [(node + 1, dist + 1), (node - 1, dist + 1), (node * 2, dist)]:
      if 0 <= i <= 100000 and (dp[i] is False or dp[i] > j):
        dp[i] = j
        q.append((i, j))

bfs()

print(dp[K])
fwefewfefe
fefef

fwefewfewfwefef