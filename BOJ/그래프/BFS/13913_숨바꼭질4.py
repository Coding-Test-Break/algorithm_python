from collections import deque
import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, M = map(int, input().split())

dist = [(-1, False) for _ in range(100_001)]

def bfs(start):
  q = deque()
  q.append(start)
  dist[start] = (0, N)

  while q:
    node = q.popleft()
    
    for n in [node + 1, node - 1, node * 2]:
      if 0 <= n <= 100_000:  
        if dist[n][0] > dist[node][0] + 1 or dist[n][0] == -1:
          q.append(n)   
          dist[n] = (dist[node][0] + 1, node)
        

def preorder(node):
  if node == N:
    print(N, end = " ")
    return
  preorder(dist[node][1])
  print(node, end = " ")

bfs(N)
print(dist[M][0])
preorder(M)