``` python
import sys
from collections import deque

N = int(input())
array = list(map(int, sys.stdin.readline().split()))
array = deque(array)
answer = []
target = 0

for _ in range(N):
    target = array.popleft()
    for i in array:
        if i > target:
            answer.append(i)
            break
    else: answer.append(-1)


for i in answer:
    print(i, end=" ")
```
