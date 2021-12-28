import sys

N, K = map(int, sys.stdin.readline().split())

if N > K:
  print(N - K)
else:
  dp = [(float('inf')) for _ in range(200001)]
  dp[N] = 0; dp[N * 2] = 1
  p = N
  for i in range(N, K + 1):
    if i >= 2 * p:
      p += 1 
    dp[i] = min(dp[i], dp[i - 1] + 1, dp[i + 1] + 1, dp[2 * p] + (2 * p) - i)
    dp[i * 2] = dp[i] + 1
    
  print(dp[K])

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 100000

dist = [0 for _ in range(MAX + 1)]

def bfs():
  q = deque()
  q.append(N)
  while q:
    current_coord = q.popleft()
    if current_coord == K:
      print(dist[K])
      break
    for i in [current_coord - 1, current_coord + 1, current_coord * 2]:
      if 0 <= i <= MAX and not dist[i]:
        dist[i] = dist[current_coord] + 1
        q.append(i)

bfs()