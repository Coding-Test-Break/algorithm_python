import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

for _ in range(T):
  M, N, K = map(int, sys.stdin.readline().split())
  worms = list()
  count = 0
  for _ in range(K):
    worms.append(tuple(map(int, sys.stdin.readline().split())))
  
  def dfs(x, y):
    try: 
      idx = worms.index(tuple([x, y]))
      worms.pop(idx)
      dfs(x - 1, y)
      dfs(x + 1, y)
      dfs(x, y - 1)
      dfs(x, y + 1)
    except ValueError:
      pass

  while worms:
    dfs(worms[0][0], worms[0][1])
    count += 1
  print(count)
