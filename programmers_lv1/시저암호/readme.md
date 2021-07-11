``` python 
def solution(s, n):
    answer = ""
    for i in s:
        if i.isupper():
            answer += chr((ord(i) - 65 + n) % 26 + 65)
        elif i.islower():
            answer += chr((ord(i) - 97 + n) % 26 + 97)
        elif i == " ": answer += " "
        
    return answer
```
- `str` 을 `list`로 변환한 후 대입 -> `"".join()` 하는 것도 방법이다. 
- ASCII 코드 !