``` python 
def solution(s):
    try:
        return int(s)
    except ValueError:
        return  (-1) * int(s[1:])
```

- try - except문에 좀 더 익숙해집시다
- int() 함수는 string 문자열 앞의 (-) 기호도 인식해서 음수로 return 한다