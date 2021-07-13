def solution(arr):
    arr.remove(sorted(arr).pop(0))
    if not arr: return [-1]
    else: return arr