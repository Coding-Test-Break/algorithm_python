import sys

A, B, C = map(int, sys.stdin.readline().split())

dp = [False for _ in range(B + 1)]
dp[1] = A
num_kv = dict()
num_kv[1] = A

def recur(pow):
  # try:
    # return num_kv[pow]
  # except KeyError:
    # pass
  # if pow == 1:
  #   return A
  if dp[pow]:
    return dp[pow]
  
  num = recur((pow + 1) // 2) * recur(pow // 2)
  # num_kv[pow] = num
  dp[pow] = num
  return num
  # return recur((pow + 1) // 2) * recur(pow // 2)

# print(recur(B) % C)
recur(B)
# print(num_kv[B] % C)
print(dp[B] % C)

