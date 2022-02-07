import sys

N = int(sys.stdin.readline())

tower = list(map(int, sys.stdin.readline().split()))
max = list()
answer = list()

for i, h in enumerate(tower):
  while max:
    height, idx = max[-1]
    if height >= h:
      max.append([h, i + 1])
      answer.append(idx)
      break
    else:
      max.pop()
  else:
    max.append([h, i + 1])
    answer.append(0)

for a in answer:
  print(a, end=" ")