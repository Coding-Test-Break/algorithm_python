``` python
import sys

A, B = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

nums = map(int, sys.stdin.readline().split())

decimal = 0
for num, pow in zip(nums, reversed(range(N))):
    decimal += num * (A ** pow)

answer = []

while decimal:
    answer.append(str(decimal % B))
    decimal = decimal // B

print(" ".join(answer[::-1]))
```
- M진법 -> N진법 변환문제