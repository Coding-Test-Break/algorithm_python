``` python
def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
            continue
        elif stack[-1] == i:
            stack.pop()
        else :
            stack.append(i)

    if stack: return 0
    else : return 1
```
- `stack`을 이용한 풀이
- 줄줄이 비교하는 경우 `stack`을 이용해보자..!

``` python
def solution_recursive(s):
    if len(s) == 0: 
        return 1
    for i in range(len(s) - 1):
        return solution_recursive(s.replace(s[i] + s[i], ""))
    else: return 0
```
- `recursive`를 이용한 풀이
- programmers에 제출할 경우 런타임 에러로 통과하지 못한다.. 
- replace랑 for문이 많아서..? 
- `재귀함수` 작성 시 return을 중간에 잘 활용하자
    - return 말고 그냥 `solution()`을 실행하고 `break`을 해주면 뒤에 문장 때문에 값이 `None`으로 나온다.