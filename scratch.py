import sys
import heapq

N = int(sys.stdin.readline())

heap = list()

for _ in range(N):
  x = int(sys.stdin.readline())
  if x == 0:
    try:
      print(heapq.heappop(heap))
    except IndexError:
      print(0)
  else: 
    heapq.heappush(heap, x)

