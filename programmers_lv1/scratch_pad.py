def solution(arr):
    arr.remove(sorted(arr).pop(0))
    if not arr: return [-1]
    else: return arr

arr = [4, 3, 2, 1]
# print(arr.sort())
# arr.sort()
# print(sorted(arr)) 
print(solution(arr))
