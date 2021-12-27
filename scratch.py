import sys

N, r, c = map(int, sys.stdin.readline().split())

def recur(r, c, count, N): 
  if N == 0:
    return count
  r_share, r_remainder = divmod(r, 2 ** (N - 1))
  c_share, c_remainder = divmod(c, 2 ** (N - 1))
  
  if (r_share, c_share) == (0, 0):
    return recur(r_remainder, c_remainder, count + 4 ** (N - 1) * 0, N - 1)
  elif (r_share, c_share) == (0, 1):
    return recur(r_remainder, c_remainder, count + 4 ** (N - 1) * 1, N - 1)
  elif (r_share, c_share) == (1, 0):
    return recur(r_remainder, c_remainder, count + 4 ** (N - 1) * 2, N - 1)
  elif (r_share, c_share) == (1, 1):
    return recur(r_remainder, c_remainder, count + 4 ** (N - 1) * 3, N - 1)

print(recur(r, c, 0, N))