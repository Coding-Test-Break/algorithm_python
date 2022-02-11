import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
knowing = list(map(int, sys.stdin.readline().split()))[1:]

people_party = [[] for _ in range(N + 1)]
party_people =[[] for _ in range(M + 1)]
party = [True for _ in range(M + 1)]
visited = [False for _ in range(N + 1)]

for party_idx in range(1, M + 1):
  info = list(map(int, sys.stdin.readline().split()))[1:]
  for i in info: 
    people_party[i].append(party_idx)
    party_people[party_idx].append(i)

def bfs():
  q = deque(knowing)

  while q:
    kp_idx = q.popleft()  
    if visited[kp_idx]:
      continue
    visited[kp_idx] = True
    for party_idx in people_party[kp_idx]:
      if party[party_idx]:
        for people_idx in party_people[party_idx]:
          q.append(people_idx)
        party[party_idx] = False
      
bfs()
print(sum(party) - 1)
