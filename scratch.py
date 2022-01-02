import sys

N = int(sys.stdin.readline().strip())

price = list(map(int, sys.stdin.readline().split()))

price.sort()

for i in range(1, N):
  price[i] += price[i - 1]

print(sum(price))



