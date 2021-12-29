import sys

N, M = map(int, sys.stdin.readline().split())

DB_dict = dict()

for _ in range(N):
  DB_dict[sys.stdin.readline().strip()] = 1

for _ in range(M):
  try:
    DB_dict[sys.stdin.readline().strip()] += 1 
  except: 
    pass

answer = sorted(filter(lambda x: DB_dict[x] >= 2, DB_dict))
for i in answer:
  print(i)