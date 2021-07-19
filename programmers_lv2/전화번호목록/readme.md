``` python
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    else:
        return True
```
- `.startswitch()` 메소드를 잘 활용해보자잉
- `A.startswitch(B, C)`
    - `A`: 찾는 대상
    - `B`: A안에 B로 시작하는게 있는지 
    - `C`: 찾기를 시작할 index. default는 0