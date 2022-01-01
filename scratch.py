import sys

N, K = map(int,sys.stdin.readline().split())
knapsack = list([0])

for _ in range(N):
  knapsack.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
  for j in range(1, K + 1):
    if j < knapsack[i][0]:
      dp[i][j] = dp[i - 1][j]
    else: 
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - knapsack[i][0]] + knapsack[i][1])

print(dp[N][K])
      