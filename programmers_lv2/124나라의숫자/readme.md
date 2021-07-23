``` python 
def solution(n):
    oneTwoFourDict = {1: "1", 2: "2", 0: "4"}
    answer = ""
    while n != 0:
        answer = oneTwoFourDict[n % 3] + answer
        if n % 3 == 0:
            n = n // 3 - 1
        else: n = n // 3
    
    return answer
```

- 쉬운 문제인데 너무 오래 걸려서 풀었다... 
- n진법 풀이 기억할 것
- `divmod()`를 이용하면, return 값으로 몫과 나머지를 한번에 받을 수 있다!