``` python 
def solution(arr):
    arr.remove(sorted(arr).pop(0))
    if not arr: return [-1]
    else: return arr
``` 
- .sort() 는 `inplace`로 list를 sort함
- sorted() 은 `inplace` = `False`로 sort된 list를 반환하고, 원래 list는 그대로. 
- 따라서 .sort()를 반환하면 `None` 값이 나온다.