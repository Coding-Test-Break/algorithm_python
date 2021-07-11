``` python
def solution(n):
    if pow(n, 1/2) % 1 == 0: return (pow(n, 1/2) + 1) ** 2
    else: return -1
```