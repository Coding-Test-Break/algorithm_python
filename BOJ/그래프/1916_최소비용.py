import heapq
import math
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

dist = [math.inf for _ in range(N + 1)]

graph = [[] for _ in range(N + 1)]

for _ in range(M):
  f, t, d = map(int, input().split()) 
  for i in range(len(graph[f])):
    if graph[f][i][0] == t:
      graph[f][i][1] = min(d, graph[f][i][1])
      break
  else: 
    graph[f].append([t, d])

START, END = map(int, input().split())
dist[START] = 0

def dijkstra(s):
  queue = list()
  heapq.heappush(queue, (dist[s], s))
  
  while queue:
    currDist, currNode = heapq.heappop(queue)
    
    for nextNode, nextDist in graph[currNode]:
      if dist[nextNode] > nextDist + currDist:
        dist[nextNode] = nextDist + currDist
        heapq.heappush(queue, (dist[nextNode], nextNode))

dijkstra(START)
print(dist[END])