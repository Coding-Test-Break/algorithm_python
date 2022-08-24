def solution(grid):
    global dx, dy, n, m, visited
    answer = list()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    n = len(grid)
    m = len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if not visited[i][j][k]:
                    answer.append(stack_dfs((i, j, k), grid))
    
    return sorted(answer)

def dfs(x, y, v, cnt, visited, grid):
    if visited[x][y][v]:
        return cnt
    visited[x][y][v] = True
    nx = 0
    ny = 0
    
    if grid[x][y] == "S":
        nx, ny = coord(x + dx[v], y + dy[v]) 
    elif grid[x][y] == "L":
        v -= 1
        if v < 0:
            v = 3
        nx, ny = coord(x + dx[v], y + dy[v])
    elif grid[x][y] == "R":
        v += 1
        if v > 3:
            v = 0
        nx, ny = coord(x + dx[v], y + dy[v])
        
    return dfs(nx, ny, v, cnt + 1, visited, grid)
    
def coord(x, y):
    if x >= n:
        x = 0
    elif x < 0:
        x = n - 1
    if y >= m:
        y = 0
    elif y < 0:
        y = m - 1
    return (x, y)

def stack_dfs(node, grid):
  i, j, k = node
  visited[i][j][k] = True
  cnt = 1
  stack = list()
  stack.append(node)
  
  while stack:
    x, y, v = stack.pop()
    nx = 0
    ny = 0
    
    if grid[x][y] == "S":
        nx, ny = coord(x + dx[v], y + dy[v]) 
    elif grid[x][y] == "L":
        v -= 1
        if v < 0:
            v = 3
        nx, ny = coord(x + dx[v], y + dy[v])
    elif grid[x][y] == "R":
        v += 1
        if v > 3:
            v = 0
        nx, ny = coord(x + dx[v], y + dy[v])

    if not visited[nx][ny][v]:
      visited[nx][ny][v] = True
      stack.append((nx, ny, v))
      cnt += 1 

  return cnt

print(solution(["SL","LR"]))

# 재귀로 푸니까 런타임 에러 나서 stack으로 풀었다.
# O(n^2) 에 dfs는 시간복잡도가 뭐지 ... stack 만큼 반복하긴 하는데 전부 다 합해도 n * m * 4 회인데 잘 모르겠다
# 아무튼 0 <= n, m < 500 이므로 O(n^3) 으로도 충분히 풀 수 있었으니까 무난하게 통과