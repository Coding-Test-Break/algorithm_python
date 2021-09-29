import sys

N = int(sys.stdin.readline())

dp = 3
temp = 0
for i in range(4, N + 1, 2):
    dp = 3 * dp + 2
    
if N % 2 == 1:
    print(0)
else: 
    print(dp)